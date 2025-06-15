# RAG-powered Chatbot Assistant

This project is a Retrieval-Augmented Generation (RAG) chatbot assistant that answers questions based on your custom document set. It uses LangChain, ChromaDB for vector storage, HuggingFace embeddings, and Groq LLM for generating responses. The app features an interactive Streamlit UI.


![RAG Chatbot Demo](./screenshots/Screenshot%202025-06-15%20181142.png)

![Chatbot UI Screenshot](./screenshots/Screenshot%202025-06-15%20181222.png)

## Features

- Loads and splits your documents from the `data/` folder
- Embeds and stores them in a persistent ChromaDB vector store
- Retrieves relevant context for user queries
- Uses a Groq LLM with a robust system prompt for safe, context-aware answers
- Interactive web UI with Streamlit

## Project Structure

```
RAGchatbot/
├── app.py                # Streamlit UI entry point
├── requirements.txt      # Python dependencies
├── .env                  # For your GROQ_API_KEY
├── data/                 # Place your custom documents here (JSON format)
├── src/
│   ├── main.py           # Core RAG pipeline logic
│   ├── prompts.py        # System prompt for the assistant
```

## Installation

1. **Clone the repository**
2. **Install dependencies**:
   ```powershell
   pip install -r requirements.txt
   ```
3. **Set up your environment**:
   - Create a `.env` file in the project root with your Groq API key:
     ```env
     GROQ_API_KEY=your-groq-api-key-here
     ```
   - Place your custom documents (JSON) in the `data/` folder.

## Running the App

Start the Streamlit UI:

```powershell
streamlit run app.py
```

Visit the local URL shown in your terminal to interact with the chatbot.

## Usage

- Enter your question in the input box and click "Ask".
- The assistant will answer using only the information from your documents.
- Chat history is displayed for your session.

## Notes

- The first run will embed and store your documents in ChromaDB. Subsequent runs will reuse the existing vector store.
- To update the knowledge base, add new documents to the `data/` directory.

## License

MIT
