"""Contoso Roastery support assistant — console interface.

Usage:
    python ingest.py   (once, to build the database)
    python main.py
"""

import config
from chat import answer_query
from foundry_client import get_client, resolve_model_id


def main():
    print("Loading models (the first run can take a minute)...")
    client = get_client()
    chat_id = resolve_model_id(client, config.CHAT_MODEL)
    embed_id = resolve_model_id(client, config.EMBEDDING_MODEL)
    print("Ready. Ask a question about Contoso Roastery products ('quit' to exit).\n")

    while True:
        try:
            question = input("You: ").strip()
        except (EOFError, KeyboardInterrupt):
            break
        if not question:
            continue
        if question.lower() in {"quit", "exit"}:
            break

        answer, chunks = answer_query(client, chat_id, embed_id, question)
        sources = ", ".join(sorted({source for source, _, _ in chunks}))
        print(f"\nAssistant: {answer}")
        print(f"(retrieved from: {sources})\n")

    print("Goodbye!")


if __name__ == "__main__":
    main()
