"""Step 1 of the RAG pipeline: read documents, split them into chunks,
compute an embedding for each chunk, and store everything in SQLite.

Run it once (and again whenever the documents change):

    python ingest.py
"""

import json
import sqlite3

import config
from foundry_client import get_client, resolve_model_id


def split_sections(text):
    """Split markdown text into (heading, body) pairs, one per heading."""
    sections, heading, lines = [], "", []
    for line in text.splitlines():
        if line.startswith("#"):
            sections.append((heading, "\n".join(lines).strip()))
            heading, lines = line.lstrip("#").strip(), []
        else:
            lines.append(line)
    sections.append((heading, "\n".join(lines).strip()))
    return [(h, b) for h, b in sections if b]


def chunk_text(text, max_chars=config.MAX_CHUNK_CHARS):
    """Split a markdown document into chunks that follow its heading
    structure. Every chunk starts with the document title and its section
    heading, so a chunk still makes sense on its own — both to the embedding
    model (better retrieval) and to the LLM (better answers). Within a long
    section, paragraphs are merged up to roughly max_chars per chunk."""
    first_line = text.strip().splitlines()[0]
    title = first_line.lstrip("#").strip() if first_line.startswith("#") else ""

    chunks = []
    for heading, body in split_sections(text):
        label = f"{title} - {heading}" if heading and heading != title else title
        paragraphs = [p.strip() for p in body.split("\n\n") if p.strip()]
        current = ""
        for paragraph in paragraphs:
            if current and len(current) + len(paragraph) > max_chars:
                chunks.append(f"[{label}]\n{current}")
                current = paragraph
            else:
                current = f"{current}\n\n{paragraph}" if current else paragraph
        if current:
            chunks.append(f"[{label}]\n{current}")
    return chunks


def create_table(db):
    """Start fresh each run so re-ingesting never duplicates rows."""
    db.execute("DROP TABLE IF EXISTS chunks")
    db.execute(
        """
        CREATE TABLE chunks (
            id        INTEGER PRIMARY KEY,
            source    TEXT NOT NULL,   -- which document the chunk came from
            content   TEXT NOT NULL,   -- the chunk text itself
            embedding TEXT NOT NULL    -- the vector, stored as a JSON list
        )
        """
    )


def main():
    if not config.DOCS_DIR.is_dir():
        raise SystemExit(f"Documents folder not found: {config.DOCS_DIR}")

    client = get_client()
    model_id = resolve_model_id(client, config.EMBEDDING_MODEL)

    db = sqlite3.connect(config.DB_PATH)
    create_table(db)

    total = 0
    for doc_path in sorted(config.DOCS_DIR.glob("*.md")):
        chunks = chunk_text(doc_path.read_text(encoding="utf-8"))
        response = client.embeddings.create(model=model_id, input=chunks)
        for chunk, item in zip(chunks, response.data):
            db.execute(
                "INSERT INTO chunks (source, content, embedding) VALUES (?, ?, ?)",
                (doc_path.name, chunk, json.dumps(item.embedding)),
            )
        total += len(chunks)
        print(f"  {doc_path.name}: {len(chunks)} chunks")

    db.commit()
    db.close()
    print(f"Done. Stored {total} chunks in {config.DB_PATH.name}.")


if __name__ == "__main__":
    main()
