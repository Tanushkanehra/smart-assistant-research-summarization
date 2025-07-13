# 📚 Smart Assistant for Research Summarization

This project is an AI-powered assistant that reads and understands research documents (PDF/TXT). It can summarize, answer questions, and challenge users logically — all grounded in the content.

## 🚀 Features

- Upload PDF/TXT files
- Auto-summarizes in ≤150 words
- “Ask Anything” mode: Free-form question answering
- “Challenge Me” mode: Logic-based Q&A with AI feedback
- Justifies all responses with document reference
- Web-based UI with Streamlit
- Optional: Memory, Highlighting (extensible)

## 🧠 Tech Stack

| Layer     | Tool              |
|-----------|-------------------|
| Frontend  | Streamlit         |
| Backend   | FastAPI           |
| NLP       | HuggingFace + OpenAI |
| Extras    | LangChain, PyPDF2 |

## 🛠 Setup

```bash
git clone https://github.com/yourname/smart-assistant-research-summarization.git
cd smart-assistant-research-summarization

python -m venv env
env\Scripts\activate  # Use `source env/bin/activate` on Linux/Mac

pip install -r requirements.txt
set OPENAI_API_KEY=your-key-here  # Or export on Unix

uvicorn backend.main:app --reload
streamlit run frontend/app.py
```

## 📊 Architecture

```
User → Streamlit UI → FastAPI Backend → HuggingFace + LangChain → Results
```

## ✅ Task Breakdown

- [x] Upload & Summarize Document
- [x] Ask Anything Mode
- [x] Challenge Me with Evaluation
- [x] Justification for All Answers

## 📽 Demo (2-min)
Coming soon: [YouTube Demo Link]

## 🧠 Authors
- Manu Nehra