"""Week 2 exercise: embeddings and similarity search.

Goal: embed a list of sentences, embed a query, and print the sentences
ranked by cosine similarity to the query. Replace each `...` following
these steps, then run:

    python embedding_demo_starter.py

Steps (each matches one `...` below, in order):
1. In cosine_similarity, implement: dot(a, b) / (norm(a) * norm(b)).
   Hint: np.dot and np.linalg.norm do the heavy lifting.
2. Embed all SENTENCES in ONE call:
   client.embeddings.create(model=model_id, input=SENTENCES),
   then collect each item.embedding from response.data into a list.
3. Embed the query the same way (input=[query] — note the list!).
4. Score every sentence against the query with cosine_similarity, sort
   best-first, and print "score  sentence" lines.

When it works, try a query that shares NO words with its best match, e.g.
"How long is the guarantee?" — what happens, and why is that better than
keyword search?
"""

import numpy as np

from foundry_client import get_client, resolve_model_id

EMBEDDING_MODEL = "qwen3-embedding-0.6b"

SENTENCES = [
    "The espresso machine takes 40 seconds to heat up.",
    "Cats are wonderful companions for city apartments.",
    "Our warranty lasts two years from the date of purchase.",
    "The soccer match ended in a dramatic penalty shootout.",
    "Steam the milk to about 60 degrees for the best flavor.",
]


def cosine_similarity(a, b):
    ...


def main():
    client = get_client()
    model_id = resolve_model_id(client, EMBEDDING_MODEL)

    vectors = ...

    query = input("Type a question or sentence: ")

    query_vector = ...

    ...


if __name__ == "__main__":
    main()
