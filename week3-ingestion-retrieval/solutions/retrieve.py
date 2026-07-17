"""Step 2 of the RAG pipeline: given a question, find the most relevant
stored chunks by comparing embedding vectors.

Try it directly:

    python retrieve.py "How often should I descale the machine?"

How it works: the question is embedded with the same model that embedded
the documents, then compared against every stored chunk with cosine
similarity (1.0 = same meaning, near 0 = unrelated). Brute-force
comparison is completely fine at our scale of a few hundred chunks; with
millions of chunks you would switch to a dedicated vector database or a
SQLite vector extension — same idea, faster lookup.
"""

import json
import sqlite3
import sys

import numpy as np

import config
from foundry_client import get_client, resolve_model_id


def cosine_similarity(a, b):
    """Return how similar two vectors point (1.0 same, ~0 unrelated)."""
    a, b = np.asarray(a), np.asarray(b)
    return float(np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b)))


def get_top_chunks(client, embed_model_id, question, k=config.TOP_K):
    """Return the k best-matching (source, content, score) tuples, best first."""
    if not config.DB_PATH.exists():
        raise SystemExit(f"Database not found: {config.DB_PATH}. Run ingest.py first.")

    query_vector = (
        client.embeddings.create(model=embed_model_id, input=[question]).data[0].embedding
    )

    db = sqlite3.connect(config.DB_PATH)
    rows = db.execute("SELECT source, content, embedding FROM chunks").fetchall()
    db.close()

    scored = [
        (source, content, cosine_similarity(query_vector, json.loads(embedding)))
        for source, content, embedding in rows
    ]
    scored.sort(key=lambda item: item[2], reverse=True)
    return scored[:k]


def main():
    question = " ".join(sys.argv[1:]).strip() or input("Question: ")
    client = get_client()
    model_id = resolve_model_id(client, config.EMBEDDING_MODEL)
    for source, content, score in get_top_chunks(client, model_id, question):
        print(f"\n--- {source}  (similarity {score:.3f}) ---")
        print(content[:300])


if __name__ == "__main__":
    main()
