"""Step 3 of the RAG pipeline: answer a question with the local LLM,
using the retrieved chunks as the only allowed source of truth.

The prompt has two parts:
- System message: defines the assistant's role, restricts it to the
  provided context, and dictates the exact fallback sentence for when the
  context does not contain the answer.
- User message: the retrieved chunks, each labeled with its source file
  (so the model can refer to it and you can debug retrieval), followed by
  the actual question.

temperature=0.2 keeps the model factual and repeatable instead of creative.
"""

import config
from foundry_client import get_client, resolve_model_id
from retrieve import get_top_chunks

SYSTEM_PROMPT = """\
You are a support assistant for Contoso Roastery products.
Answer the user's question using ONLY the information in the provided context.
If the context does not contain the answer, reply exactly:
"I don't have that information in my documents."
Keep answers short and factual."""


def build_user_message(question, chunks):
    """Pack the retrieved chunks and the question into one prompt."""
    context = "\n\n".join(f"[{source}]\n{content}" for source, content, _ in chunks)
    return f"Context:\n{context}\n\nQuestion: {question}"


def answer_query(client, chat_model_id, embed_model_id, question):
    """Run the full RAG round trip: retrieve, augment, generate.
    Returns (answer_text, retrieved_chunks)."""
    chunks = get_top_chunks(client, embed_model_id, question)
    response = client.chat.completions.create(
        model=chat_model_id,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": build_user_message(question, chunks)},
        ],
        max_tokens=400,
        temperature=0.2,
    )
    return response.choices[0].message.content.strip(), chunks
