import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

import streamlit as st
from src.main import retrieve_and_answer, collection, embeddings, llm

st.set_page_config(page_title="RAG Chatbot", page_icon="🤖")
st.title("RAG-powered Assistant")

if "history" not in st.session_state:
    st.session_state["history"] = []

user_input = st.text_input("Ask a question about your documents:", "")

if st.button("Ask") and user_input:
    with st.spinner("Thinking..."):
        answer = retrieve_and_answer(user_input, collection, embeddings, llm)
        st.session_state["history"].append((user_input, answer))

if st.session_state["history"]:
    st.subheader("Chat History")
    for q, a in reversed(st.session_state["history"]):
        st.markdown(f"**You:** {q}")
        st.markdown(f"**Assistant:** {a}")
