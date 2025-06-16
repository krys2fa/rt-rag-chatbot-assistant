# RAG-powered AI Assistant
A modern Retrieval-Augmented Generation (RAG) AI chatbot that answers questions using your own documents!  
Built with [LangChain](https://python.langchain.com/), [ChromaDB](https://www.trychroma.com/), [HuggingFace Embeddings](https://huggingface.co/sentence-transformers), [Groq LLM](https://groq.com/), and [Streamlit](https://streamlit.io/).


![RAG Chatbot Demo](./screenshots/Screenshot%202025-06-15%20181142.png)


## Abstract

This project presents a Retrieval-Augmented Generation (RAG) chatbot assistant that leverages custom document sets to provide contextually accurate answers. By integrating LangChain, ChromaDB, HuggingFace embeddings, Groq LLM, and Streamlit, the assistant demonstrates a modern, modular approach to building AI-powered, domain-specific conversational agents. The solution is designed for extensibility, reproducibility, and ease of use, making it suitable for both research and practical deployment.

## Introduction

Large Language Models (LLMs) have revolutionized natural language understanding and generation, but they often lack access to up-to-date or domain-specific knowledge. Retrieval-Augmented Generation (RAG) addresses this limitation by combining LLMs with external knowledge sources, enabling more accurate and grounded responses. This project implements a RAG pipeline that allows users to query their own document collections through a user-friendly web interface. The assistant is built using Python and leverages state-of-the-art open-source tools for vector search, embedding, and LLM orchestration.

## Methodology

The RAG-powered chatbot is implemented using the following pipeline:

1. **Document Ingestion & Chunking:**
   - Custom documents in JSON format are loaded from the `data/` directory.
   - Documents are split into manageable text chunks using LangChain's `RecursiveCharacterTextSplitter` for optimal retrieval granularity.

2. **Embedding & Vector Storage:**
   - Each text chunk is embedded using HuggingFace's `sentence-transformers/all-MiniLM-L6-v2` model.
   - Embeddings and their corresponding text are stored in a persistent ChromaDB vector store, enabling fast and scalable similarity search.

3. **Query Processing & Retrieval:**
   - User queries are embedded using the same embedding model.
   - The top-k most relevant document chunks are retrieved from ChromaDB based on cosine similarity.

4. **Prompt Formulation & LLM Response:**
   - Retrieved context is combined with a robust, safety-focused system prompt.
   - The prompt and user question are sent to the Groq LLM (Llama 3.1) via API.
   - The LLM generates a response, strictly grounded in the retrieved context.

5. **User Interface:**
   - Streamlit provides an interactive web UI for users to input questions and view responses.
   - Chat history is maintained for each session, enhancing usability.

This modular approach ensures that the assistant is both extensible and maintainable, with clear separation between data ingestion, retrieval, and generation components.

---

## Features

- **Custom Knowledge Base:** Answers are grounded in your own documents (JSON in `/data`).
- **Fast Vector Search:** Uses ChromaDB for persistent, efficient retrieval.
- **Modern LLM:** Integrates Groq’s Llama 3.1 for high-quality, safe responses.
- **Interactive UI:** Chat with your data using a beautiful Streamlit interface.
- **Easy Setup:** Just add your docs, set your API key, and run!

---

## Project Structure

```text
RAGchatbot/
├── app.py                # Streamlit UI entry point
├── requirements.txt      # Python dependencies
├── .env                  # For your GROQ_API_KEY
├── data/                 # Your custom documents (JSON)
├── src/
│   ├── main.py           # Core RAG pipeline logic
│   ├── prompts.py        # System prompt for the assistant
```

---

## Installation

1. **Clone the repository**
2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```
3. **Set up your environment**
   - Copy `.env_example` to `.env` and add your Groq API key:
     ```env
     GROQ_API_KEY=your-groq-api-key-here
     ```
   - Place your custom JSON documents in the `data/` folder.

---

## Usage

Start the Streamlit app:

```bash
streamlit run app.py
```

Open the local URL in your browser.  
Type your question in the input box and click “Ask.”  
The assistant will answer using only your documents.  
Chat history is displayed for your session.

---

## Example Code

```python
from src.main import retrieve_and_answer, collection, embeddings, llm

query = "What are variational autoencoders?"
answer = retrieve_and_answer(query, collection, embeddings, llm)
print(answer)
```

---

## Screenshots

![Chatbot UI Screenshot](./screenshots/Screenshot%202025-06-15%20181222.png)

---

## Learn More

- [LangChain Documentation](https://python.langchain.com/)
- [ChromaDB Docs](https://docs.trychroma.com/)
- [Groq LLM](https://groq.com/)
- [Streamlit Docs](https://docs.streamlit.io/)

---

## License

MIT

---

Feel free to add more images, code snippets, or links to your demo, dataset, or related publications!
