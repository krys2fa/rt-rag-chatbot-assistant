# RAG-powered AI Assistant

A modern Retrieval-Augmented Generation (RAG) AI chatbot that answers questions using your own documents!  
Built with [LangChain](https://python.langchain.com/), [ChromaDB](https://www.trychroma.com/), [HuggingFace Embeddings](https://huggingface.co/sentence-transformers), [Groq LLM](https://groq.com/), and [Streamlit](https://streamlit.io/).



![RAG Chatbot Demo](./screenshots/Screenshot%202025-06-15%20181142.png)

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
