"""Week 3 exercise: the retrieval function.

Goal: given a question, return the TOP_K most relevant chunks from the
database your ingestion script built. Replace each `...` in
get_top_chunks following these steps, then test:

    python retrieve_starter.py "How often should I descale the machine?"
    python retrieve_starter.py "What grinder setting for French press?"

Steps (each matches one `...` below, in order):
1. Embed the question (input=[question] — note the list!).
2. SELECT source, content, embedding FROM chunks. Remember the stored
   embedding is JSON text, so json.loads(...) it back to a list.
3. Score every row with cosine_similarity, sort descending, and return
   the first k as (source, content, score) tuples.

Test with questions you KNOW the docs answer: the top result should come
from the right document with similarity > 0.5.
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
    """Return the k most relevant (source, content, score) tuples, best first."""
    query_vector = ...

    rows = ...

    ...


def main():
    question = " ".join(sys.argv[1:]).strip() or input("Question: ")
    client = get_client()
    model_id = resolve_model_id(client, config.EMBEDDING_MODEL)
    for source, content, score in get_top_chunks(client, model_id, question):
        print(f"\n--- {source}  (similarity {score:.3f}) ---")
        print(content[:300])


if __name__ == "__main__":
    main()
