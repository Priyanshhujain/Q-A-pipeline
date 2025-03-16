from transformers import pipeline
MODEL_OPTIONS = {
    "T5 Small": "t5-small",
    "DistilGPT-2": "distilgpt2",
    "BART Base": "facebook/bart-base",
    "FLAN-T5 Small": "google/flan-t5-small",
    "GPT-Neo 125M": "EleutherAI/gpt-neo-125M"
}
def generate_answer(context, question, model_name):
    if model_name not in MODEL_OPTIONS.values():
        raise ValueError("Invalid model selection.")
    generator = pipeline("text-generation", model=model_name, device=-1)
    prompt = f"""
    Context:
    {context}
    Question: {question}
    Instructions:
    - Provide a structured and concise answer.
    - Highlight real-world applications.
    - Avoid vague responses.
    Answer:
    """
    output = generator(prompt, max_new_tokens=300)
    return output[0]['generated_text']