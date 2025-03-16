import sys
import os
import streamlit as st
from main import run_pipeline
from modules.generation import MODEL_OPTIONS

st.title("📚 AI-Powered Q&A Agent")
model_name = st.selectbox("Select a Pretrained Model:", list(MODEL_OPTIONS.keys()))
query = st.text_input("Ask a question:")
if st.button("Get Answer"):
    if query:
        response = run_pipeline(query, MODEL_OPTIONS[model_name])
        st.write("### Answer")
        st.write(response["Answer"])
        st.write("### Chain of Thought Reasoning")
        st.write(response["Chain_of_Thought"])
        st.write("### Evaluation Metrics")
        for metric, value in response["Evaluation_Metrics"].items():
            st.write(f"**{metric}:** {value:.2f}")
        st.write("### Model Used")
        st.write(response["Model Used"])