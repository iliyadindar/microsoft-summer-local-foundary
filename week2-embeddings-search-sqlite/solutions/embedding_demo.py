"""Week 2: turn sentences into vectors and find the most similar one.

    python embedding_demo.py

What to observe:
- One embeddings API call can embed a whole list of texts at once.
- The top match shares MEANING with your query even when it shares no
  words (try "How long is the guarantee?" against the warranty sentence).
  That is what makes embeddings better than keyword search for the
  retrieval step of RAG.
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
    """Return how similar two vectors point (1.0 same, ~0 unrelated)."""
    a, b = np.asarray(a), np.asarray(b)
    return float(np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b)))


def main():
    client = get_client()
    model_id = resolve_model_id(client, EMBEDDING_MODEL)

    response = client.embeddings.create(model=model_id, input=SENTENCES)
    vectors = [item.embedding for item in response.data]
    print(f"Embedded {len(SENTENCES)} sentences; each vector has {len(vectors[0])} numbers.\n")

    query = input("Type a question or sentence: ").strip() or "How long is the guarantee?"
    query_vector = (
        client.embeddings.create(model=model_id, input=[query]).data[0].embedding
    )

    scored = sorted(
        zip(SENTENCES, (cosine_similarity(query_vector, v) for v in vectors)),
        key=lambda pair: pair[1],
        reverse=True,
    )
    print(f"\nMost similar to: \"{query}\"\n")
    for sentence, score in scored:
        print(f"  {score:.3f}  {sentence}")


if __name__ == "__main__":
    main()
