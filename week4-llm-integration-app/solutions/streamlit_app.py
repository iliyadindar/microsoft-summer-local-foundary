"""Stretch goal: the same assistant with a web interface.

    pip install streamlit
    streamlit run streamlit_app.py

Everything still runs locally — Streamlit just serves the page to your browser.
"""

import streamlit as st

import config
from chat import answer_query
from foundry_client import get_client, resolve_model_id


@st.cache_resource
def load_models():
    client = get_client()
    chat_id = resolve_model_id(client, config.CHAT_MODEL)
    embed_id = resolve_model_id(client, config.EMBEDDING_MODEL)
    return client, chat_id, embed_id


st.title("☕ Contoso Roastery Support Assistant")
st.caption("Runs 100% on this machine with Foundry Local — no internet needed.")

client, chat_id, embed_id = load_models()

if "history" not in st.session_state:
    st.session_state.history = []

for role, text in st.session_state.history:
    st.chat_message(role).write(text)

if question := st.chat_input("Ask about Contoso Roastery products"):
    st.chat_message("user").write(question)
    with st.spinner("Thinking..."):
        answer, chunks = answer_query(client, chat_id, embed_id, question)
    sources = ", ".join(sorted({source for source, _, _ in chunks}))
    reply = f"{answer}\n\n*Retrieved from: {sources}*"
    st.chat_message("assistant").write(reply)
    st.session_state.history += [("user", question), ("assistant", reply)]
