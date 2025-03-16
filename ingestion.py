import os
import pickle
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
from PyPDF2 import PdfReader

VECTOR_STORE_PATH = "data/vector_store.pkl"
model = SentenceTransformer("all-MiniLM-L6-v2")  # Small model, no API needed

def extract_text(pdf_path):
    with open(pdf_path, "rb") as file:
        reader = PdfReader(file)
        text = "\n".join([page.extract_text() for page in reader.pages if page.extract_text()])
    return text

def vectorize_text(text):
    sentences = text.split(". ")  # Simple sentence splitting
    embeddings = model.encode(sentences)
    return sentences, embeddings

def save_faiss_index(embeddings, sentences):
    index = faiss.IndexFlatL2(embeddings.shape[1])
    index.add(np.array(embeddings))
    with open(VECTOR_STORE_PATH, "wb") as f:
        pickle.dump((index, sentences), f)

if __name__ == "__main__":
    pdf_text = extract_text("data/uploaded.pdf")
    sentences, embeddings = vectorize_text(pdf_text)
    save_faiss_index(embeddings, sentences)
    print("✅ Vector database created!")