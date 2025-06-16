import chromadb
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, SystemMessage
from dotenv import load_dotenv
import os
import sys
import json
from PyPDF2 import PdfReader

load_dotenv()

# --- System Prompt ---
SYSTEM_PROMPT = (
    "You are an investor readiness assistant for Ghana. "
    "Use only the uploaded documents (from GIPC, Bank of Ghana, and World Bank) to answer questions about hot sectors, regulations, and investment opportunities. "
    "If the answer is not in the documents, say so."
)

# --- PDF Extraction ---
def extract_text_from_pdf(pdf_path: str) -> str:
    """
    Extracts and concatenates text from all pages of a PDF file.
    """
    reader = PdfReader(pdf_path)
    text = ""
    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text + "\n"
    return text

# --- ChromaDB Setup ---
client = chromadb.PersistentClient(path="./data")
collection = client.get_or_create_collection(
    name="ml_publications",
    metadata={"hnsw:space": "cosine"}
)

# --- Embedding Model ---
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# --- PDF Ingestion & Chunking ---
PDF_PATH = os.path.join(os.path.dirname(__file__), '..', 'data', 'Summary-of-Economic-and-Financial-Data-May-2025.pdf')
pdf_text = extract_text_from_pdf(PDF_PATH)
print("\n[DEBUG] First 1000 characters of extracted PDF text:\n", pdf_text[:1000])

splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
document_chunks = splitter.split_text(pdf_text)
print(f"Loaded and split {len(document_chunks)} text chunks from PDF.")

# --- Add Chunks to ChromaDB ---
def add_chunks_to_chromadb(chunks, collection, embeddings):
    """
    Embeds and adds text chunks to the ChromaDB collection.
    """
    ids = [f"chunk-{i}" for i in range(len(chunks))]
    vectors = embeddings.embed_documents(chunks)
    collection.add(
        documents=chunks,
        embeddings=vectors,
        ids=ids
    )
    print(f"Added {len(chunks)} chunks to ChromaDB collection '{collection.name}'.")

if collection.count() == 0:
    add_chunks_to_chromadb(document_chunks, collection, embeddings)
else:
    print(f"Collection '{collection.name}' already contains {collection.count()} documents.")

# --- LLM Setup ---
llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0.7,
    api_key=os.getenv("GROQ_API_KEY")
)

# --- Retrieval & Answer Generation ---
def retrieve_and_answer(query: str, collection, embeddings, llm, top_k: int = 4) -> str:
    """
    Embeds the query, retrieves top_k similar chunks, and generates an LLM answer.
    """
    query_embedding = embeddings.embed_query(query)
    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=top_k
    )
    retrieved_chunks = [doc for doc in results['documents'][0]]
    context = '\n'.join(retrieved_chunks)
    print("\n[DEBUG] Top retrieved context for query '", query, "':\n", context[:1000])
    prompt = (
        f"Answer the following question using only the context below.\n\nContext:\n{context}\n\nQuestion: {query}\n\n"
        "If the answer is not in the context, say 'I'm sorry, that information is not in this publication.'"
    )
    messages = [
        SystemMessage(content=SYSTEM_PROMPT),
        HumanMessage(content=prompt)
    ]
    response = llm.invoke(messages)
    return response.content