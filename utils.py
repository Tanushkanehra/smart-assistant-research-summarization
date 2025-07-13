from transformers import pipeline
from PyPDF2 import PdfReader
from langchain.chat_models import ChatOpenAI
import os
import json

llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.5)

qa_model = pipeline("question-answering", model="distilbert-base-uncased-distilled-squad")
summarizer = pipeline("summarization")

def extract_text(path):
    if path.endswith(".pdf"):
        reader = PdfReader(path)
        return "\n".join(page.extract_text() for page in reader.pages)
    else:
        with open(path, "r", encoding="utf-8") as f:
            return f.read()

def generate_summary(text):
    return summarizer(text[:1000])[0]["summary_text"]

def ask_question(context, question):
    result = qa_model(question=question, context=context)
    return result["answer"], f"Based on: '{result['answer']}'"

def generate_challenge_questions(text):
    prompt = f"""
Read the document and generate 3 logic-based questions with answers.

Document:
{text[:2000]}

Respond in JSON format like:
[{{"question": "...", "answer": "..."}}]
"""
    try:
        response = llm.predict(prompt)
        return json.loads(response)
    except:
        return [{"question": "Error generating questions", "answer": ""}]

def evaluate_answer(text, user_ans, expected_ans, question):
    prompt = f"""
Evaluate the user's answer.

Document: {text[:2000]}
Question: {question}
Expected: {expected_ans}
User: {user_ans}

Respond with:
- Verdict: Correct/Incorrect/Partial
- Justification: ...
"""
    return llm.predict(prompt)