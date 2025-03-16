import os
import json
import faiss
import numpy as np
from modules.ingestion import extract_text, vectorize_text
from modules.retrieval import retrieve_relevant_chunks
from modules.reranking import rerank_results
from modules.generation import generate_answer, MODEL_OPTIONS
from modules.evaluation import compute_metrics
from modules.chain_of_thought import chain_of_thought_reasoning

def run_pipeline(query, model_name):
    retrieved_chunks = retrieve_relevant_chunks(query)
    reranked_chunks = rerank_results(query, retrieved_chunks)
    context = " ".join(reranked_chunks) if reranked_chunks else "No relevant context found."
    answer = generate_answer(context, query, model_name) if context != "No relevant context found." else "I couldn't find relevant information."
    cot_reasoning = chain_of_thought_reasoning(query, context)
    metrics = compute_metrics(answer, context)
    output = {
        "Answer": answer,
        "Chain_of_Thought": cot_reasoning,
        "Evaluation_Metrics": metrics,
        "Model Used": model_name
    }
    return output

if __name__ == "__main__":
    print("\n🔹 Welcome to the AI-Powered Q&A Pipeline 🔹\n")
    print("Available Models:")
    for i, model in enumerate(MODEL_OPTIONS.keys(), 1):
        print(f"{i}. {model}")
    
    model_choice = int(input("\nSelect a model (Enter number): "))
    model_name = list(MODEL_OPTIONS.values())[model_choice - 1]
    
    while True:
        query = input("\nAsk a question (or type 'exit' to quit): ")
        if query.lower() == "exit":
            print("\n🔹 Exiting... Thank you for using the AI Q&A Pipeline! 🔹\n")
            break
        run_pipeline(query, model_name)