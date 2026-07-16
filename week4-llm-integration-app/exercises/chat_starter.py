"""Week 4 exercise: connect retrieval to the LLM.

Goal: implement answer_query() — the full RAG round trip:
retrieve chunks, pack them into a prompt, get the model's answer.

Copy your working ingest.py / retrieve.py / config.py / foundry_client.py
from Week 3 into this folder first (or use the Week 3 solutions).

Fill in the TODOs, then run:  python chat_starter.py
"""

import config
from foundry_client import get_client, resolve_model_id
from retrieve import get_top_chunks

# TODO 1: write the system prompt. It must tell the model to:
#   - answer ONLY from the provided context
#   - say "I don't have that information in my documents." when the
#     context doesn't contain the answer
#   - keep answers short
SYSTEM_PROMPT = """..."""


def build_user_message(question, chunks):
    # TODO 2: format the chunks into a context block. Label each chunk with
    # its source file, e.g.:
    #   [manual.md]
    #   <chunk text>
    # then append "Question: <question>" at the end.
    ...


def answer_query(client, chat_model_id, embed_model_id, question):
    # TODO 3: retrieve chunks with get_top_chunks(...), then call
    # client.chat.completions.create with BOTH a system and a user message.
    # Use temperature=0.2 — why low? (Discuss with your team.)
    # Return (answer_text, chunks).
    ...


def main():
    client = get_client()
    chat_id = resolve_model_id(client, config.CHAT_MODEL)
    embed_id = resolve_model_id(client, config.EMBEDDING_MODEL)

    # A quick end-to-end test — one answerable, one unanswerable:
    for question in [
        "How often should I replace the water filter?",
        "Does the Aurora X1 have Bluetooth?",
    ]:
        answer, chunks = answer_query(client, chat_id, embed_id, question)
        print(f"\nQ: {question}\nA: {answer}")


if __name__ == "__main__":
    main()
