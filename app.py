import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

import streamlit as st
from src.main import retrieve_and_answer, collection, embeddings, llm

st.set_page_config(page_title="Ghana Investment Insights", page_icon="🇬🇭")
st.markdown("""
<style>
    .main {background-color: #f7f7f7;}
    .stButton>button {background-color: #006400; color: white; font-weight: bold;}
    .stTextInput>div>div>input {background-color: #e8f5e9;}
</style>
""", unsafe_allow_html=True)

st.image("https://upload.wikimedia.org/wikipedia/commons/1/19/Flag_of_Ghana.svg", width=80)
st.title("Ghana Investment Insights Portal")
st.caption("Explore sector trends, economic data, and regulatory updates from official Ghanaian sources.")

with st.expander("ℹ️ About this Portal", expanded=False):
    st.write("""
        This portal helps investors, analysts, and policymakers explore Ghana's economic landscape using official Bank of Ghana reports. 
        Ask about sector performance, macroeconomic indicators, or regulatory changes. All answers are grounded in the latest uploaded report.
    """)

if "history" not in st.session_state:
    st.session_state["history"] = []

user_input = st.text_input("Type your question about Ghana's economy, sectors, or regulations:", "")

col1, col2 = st.columns([1, 5])
with col1:
    if st.button("Get Insights") and user_input:
        with st.spinner("Analyzing official data..."):
            answer = retrieve_and_answer(user_input, collection, embeddings, llm)
            st.session_state["history"].append((user_input, answer))

with col2:
    st.write("")

if st.session_state["history"]:
    st.subheader("Recent Questions & Insights")
    for q, a in reversed(st.session_state["history"]):
        st.markdown(f"<div style='background:#fff;padding:10px 15px;border-radius:8px;margin-bottom:10px;'><b>Q:</b> {q}<br><b>A:</b> {a}</div>", unsafe_allow_html=True)
