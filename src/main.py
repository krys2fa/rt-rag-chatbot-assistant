import chromadb
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
import os
import json

# Initialize ChromaDB
client = chromadb.PersistentClient(path="./data")
collection = client.get_or_create_collection(
    name="ml_publications",
    metadata={"hnsw:space": "cosine"}
)

# Set up our embedding model
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

def load_and_split_documents(data_folder: str, chunk_size: int = 500, chunk_overlap: int = 50):
    """
    Loads and splits documents from the specified folder using a text splitter.
    Returns a list of text chunks.
    """
    splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    all_chunks = []
    for filename in os.listdir(data_folder):
        if filename.endswith('.json'):
            with open(os.path.join(data_folder, filename), 'r', encoding='utf-8') as f:
                docs = json.load(f)
                for doc in docs:
                    # Use publication_description or other relevant field
                    text = doc.get('publication_description', '')
                    if text:
                        chunks = splitter.split_text(text)
                        all_chunks.extend(chunks)
    return all_chunks

# Step 2: Embed and add chunks to ChromaDB

def add_chunks_to_chromadb(chunks, collection, embeddings):
    """
    Embeds and adds text chunks to the ChromaDB collection.
    """
    ids = [f"chunk-{i}" for i in range(len(chunks))]
    vectors = embeddings.embed_documents(chunks)
    # Chroma expects: documents, embeddings, ids
    collection.add(
        documents=chunks,
        embeddings=vectors,
        ids=ids
    )
    print(f"Added {len(chunks)} chunks to ChromaDB collection '{collection.name}'.")

# Only add if collection is empty (avoid duplicates)
if collection.count() == 0:
    add_chunks_to_chromadb(document_chunks, collection, embeddings)
else:
    print(f"Collection '{collection.name}' already contains {collection.count()} documents.")

# Example usage
DATA_FOLDER = os.path.join(os.path.dirname(__file__), '..', 'data')
document_chunks = load_and_split_documents(DATA_FOLDER)
print(f"Loaded and split {len(document_chunks)} text chunks from data folder.")