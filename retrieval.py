import pickle
import numpy as np
import faiss
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")
VECTOR_STORE_PATH = "data/vector_store.pkl"

def retrieve_relevant_chunks(query, top_k=5):
    with open(VECTOR_STORE_PATH, "rb") as f:
        index, sentences = pickle.load(f)
    
    query_embedding = model.encode([query])
    distances, indices = index.search(query_embedding, top_k)
    
    return [sentences[i] for i in indices[0]]