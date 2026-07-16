"""Week 3 exercise: the ingestion pipeline.

Goal: read every markdown file in sample-docs/, split it into chunks,
embed each chunk, and store (source, content, embedding) rows in SQLite.

Fill in the TODOs, then run:  python ingest_starter.py
Check your work: the final print should report 15-35 chunks total
(the reference solution produces 27).
"""

import json
import sqlite3

import config
from foundry_client import get_client, resolve_model_id


def split_sections(text):
    """Split markdown text into (heading, body) pairs, one per heading.
    Provided for you - read it and make sure you see what it does."""
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
    """Split a markdown document into chunks that follow its headings."""
    first_line = text.strip().splitlines()[0]
    title = first_line.lstrip("#").strip() if first_line.startswith("#") else ""

    chunks = []
    for heading, body in split_sections(text):
        label = f"{title} - {heading}" if heading and heading != title else title
        paragraphs = [p.strip() for p in body.split("\n\n") if p.strip()]
        # TODO 1: walk the paragraphs, merging consecutive ones into a chunk
        # until adding the next would exceed max_chars; then start a new
        # chunk. Start every finished chunk with f"[{label}]\n" so it keeps
        # its context, and don't lose the final chunk of each section!
        ...
    return chunks


def main():
    client = get_client()
    model_id = resolve_model_id(client, config.EMBEDDING_MODEL)

    db = sqlite3.connect(config.DB_PATH)

    # TODO 2: (re)create the chunks table:
    #   id INTEGER PRIMARY KEY, source TEXT, content TEXT, embedding TEXT
    # Drop it first so re-running never duplicates rows.
    ...

    total = 0
    for doc_path in sorted(config.DOCS_DIR.glob("*.md")):
        text = doc_path.read_text(encoding="utf-8")

        # TODO 3: chunk the text, embed ALL chunks in one API call, and
        # insert one row per chunk. Store the vector as JSON text:
        #   json.dumps(item.embedding)
        ...

    db.commit()
    db.close()
    print(f"Done. Stored {total} chunks in {config.DB_PATH.name}.")


if __name__ == "__main__":
    main()
