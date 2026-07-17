"""Week 4 exercise: connect retrieval to the LLM.

Goal: implement answer_query() — the full RAG round trip: retrieve
chunks, pack them into a prompt, get the model's answer.

Copy your working ingest.py / retrieve.py from Week 3 into this folder
first (or use the Week 3 solutions; config.py and foundry_client.py are
already provided here). Replace each `...` following these steps, then:

    python chat_starter.py

Steps (each matches one `...` below, in order):
1. Write the SYSTEM_PROMPT. It must tell the model to:
   - answer ONLY from the provided context
   - say "I don't have that information in my documents." when the
     context doesn't contain the answer
   - keep answers short
2. In build_user_message: format the chunks into a context block. Label
   each chunk with its source file, e.g.:
       [manual.md]
       <chunk text>
   then append "Question: <question>" at the end.
3. In answer_query: retrieve chunks with get_top_chunks(...), then call
   client.chat.completions.create with BOTH a system and a user message.
   Use temperature=0.2 — why low? (Discuss with your team.)
   Return (answer_text, chunks).

main() runs a quick end-to-end test: one answerable question, one
unanswerable one.
"""

import config
from foundry_client import get_client, resolve_model_id
from retrieve import get_top_chunks

SYSTEM_PROMPT = """..."""


def build_user_message(question, chunks):
    ...


def answer_query(client, chat_model_id, embed_model_id, question):
    ...


def main():
    client = get_client()
    chat_id = resolve_model_id(client, config.CHAT_MODEL)
    embed_id = resolve_model_id(client, config.EMBEDDING_MODEL)

    for question in [
        "How often should I replace the water filter?",
        "Does the Aurora X1 have Bluetooth?",
    ]:
        answer, chunks = answer_query(client, chat_id, embed_id, question)
        print(f"\nQ: {question}\nA: {answer}")


if __name__ == "__main__":
    main()
