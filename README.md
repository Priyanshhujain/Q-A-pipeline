# 🔹 Q&A Pipeline

## 📌 Overview
This project is an **AI-powered Q&A system** that allows users to ask questions and get answers based on retrieved and reranked context. The system supports multiple **pretrained language models** (T5, GPT-2, BART, FLAN-T5, GPT-Neo) and works via:
1. **Command Line Interface (CLI)** (using `main.py`)
2. **Streamlit Web App** (using `streamlit_app.py`)

---

## 🚀 Features
✅ **Retrieves and reranks relevant text chunks** using FAISS and Sentence Transformers.  
✅ **Supports multiple pretrained models** (T5, GPT-2, BART, etc.).  
✅ **Interactive CLI mode** for direct pipeline execution.  
✅ **Streamlit UI for an easy-to-use web interface**.  
✅ **Evaluation metrics included** (Precision, Recall, Toxicity Score).  
✅ **Chain of Thought (CoT) reasoning for enhanced responses**.  
✅ **Lightweight and CPU-friendly** (no API keys required).  

---

## 🛠️ Installation & Setup
### **1️⃣ Install Dependencies**
```bash
pip install -r requirements.txt
```

### **2️⃣ Ensure Correct Project Structure**
```
/your_project/
│── main.py  
│── streamlit_app.py  
│── requirements.txt  
│── modules/  
│   │── __init__.py  
│   │── generation.py  
│   │── ingestion.py  
│   │── retrieval.py  
│   │── reranking.py  
│   │── evaluation.py  
│   │── chain_of_thought.py  
```

---

## 🎯 Usage
### **1️⃣ Run in CLI Mode**
```bash
python main.py
```
📌 **Features:**
- Select a pretrained model.
- Ask a question.
- View structured answers with reasoning & evaluation metrics.
- Type `exit` to quit.

### **2️⃣ Run Streamlit Web App**
```bash
streamlit run streamlit_app.py
```
📌 **Features:**
- Enter a question.
- Select a model from the dropdown.
- Get a structured response, CoT reasoning, and evaluation metrics.

---

## 🤖 Supported Pretrained Models
| Model Name | Type | Purpose |
|------------|------|---------|
| `t5-small` | Seq2Seq | Good for concise text generation |
| `distilgpt2` | GPT | Lightweight GPT-2 variant |
| `facebook/bart-base` | Seq2Seq | Balanced performance |
| `google/flan-t5-small` | Instruction-based | Fine-tuned for question answering |
| `EleutherAI/gpt-neo-125M` | GPT | Smallest GPT-Neo model for CPU |

---

## ⚡ Next Steps & Improvements
🔹 Add support for **custom datasets**.  
🔹 Optimize performance with **quantization**.  
🔹 Deploy Streamlit app **online**.  

---

## 🎯 Credits
Developed by **Priyanshu Jain** with guidance from AI-powered assistance. 🚀

