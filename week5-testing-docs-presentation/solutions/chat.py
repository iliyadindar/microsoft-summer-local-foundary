"""Step 3 of the RAG pipeline: answer a question with the local LLM,
using the retrieved chunks as the only allowed source of truth.

Week 5 refinements over the Week 4 version:
- the model is asked to cite the source document it used
- the fallback sentence is kept EXACT so evaluate.py can detect it

The prompt has two parts:
- System message: defines the assistant's role, restricts it to the
  provided context, dictates the exact fallback sentence, and asks for a
  source citation at the end of each answer.
- User message: the retrieved chunks, each labeled with its source file
  (so the model can cite it), followed by the actual question.

temperature=0.2 keeps the model factual and repeatable instead of creative.
"""

from retrieve import get_top_chunks

FALLBACK_ANSWER = "I don't have that information in my documents."

SYSTEM_PROMPT = f"""\
You are a support assistant for Contoso Roastery products.
Answer the user's question using ONLY the information in the provided context.
End your answer with the source in parentheses, like: (source: manual.md)
If the context does not contain the answer, reply exactly:
"{FALLBACK_ANSWER}"
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
