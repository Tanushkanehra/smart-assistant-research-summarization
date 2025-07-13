import streamlit as st
import requests

st.set_page_config(page_title="Smart Assistant", layout="centered")
st.title("📚 Smart Assistant for Research Summarization")

if "summary" not in st.session_state:
    st.session_state.summary = ""

uploaded = st.file_uploader("Upload PDF or TXT", type=["pdf", "txt"])

if uploaded:
    res = requests.post("http://localhost:8000/upload/", files={"file": uploaded})
    st.session_state.summary = res.json()["summary"]
    st.success("Document uploaded and summarized.")

st.subheader("📄 Summary")
st.write(st.session_state.summary)

mode = st.radio("Choose a mode", ["Ask Anything", "Challenge Me"])

if mode == "Ask Anything":
    question = st.text_input("Ask a question based on the document")
    if st.button("Submit"):
        res = requests.post("http://localhost:8000/ask/", json={"question": question})
        st.write("**Answer:**", res.json()["answer"])
        st.caption(res.json()["reference"])

elif mode == "Challenge Me":
    if st.button("Generate Questions"):
        questions = requests.get("http://localhost:8000/challenge/").json()["questions"]
        for i, q in enumerate(questions):
            st.markdown(f"**Q{i+1}:** {q['question']}")
            user_ans = st.text_input(f"Your Answer to Q{i+1}", key=f"user{i}")
            if user_ans:
                res = requests.post("http://localhost:8000/evaluate/", json={
                    "user_answer": user_ans,
                    "correct_answer": q['answer'],
                    "question": q['question']
                })
                st.markdown("🧠 " + res.json()["evaluation"])