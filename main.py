from fastapi import FastAPI, UploadFile, File, Body
from fastapi.middleware.cors import CORSMiddleware
from utils import extract_text, generate_summary, ask_question, generate_challenge_questions, evaluate_answer

app = FastAPI()
document_text = ""

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], allow_credentials=True,
    allow_methods=["*"], allow_headers=["*"],
)

@app.post("/upload/")
async def upload(file: UploadFile = File(...)):
    global document_text
    content = await file.read()
    doc_type = file.filename.split(".")[-1]

    with open(f"temp.{doc_type}", "wb") as f:
        f.write(content)

    document_text = extract_text(f"temp.{doc_type}")
    summary = generate_summary(document_text)
    return {"summary": summary}

@app.post("/ask/")
async def ask(query: dict):
    answer, ref = ask_question(document_text, query["question"])
    return {"answer": answer, "reference": ref}

@app.get("/challenge/")
async def challenge():
    return {"questions": generate_challenge_questions(document_text)}

@app.post("/evaluate/")
async def evaluate(data: dict = Body(...)):
    return {
        "evaluation": evaluate_answer(
            document_text,
            data["user_answer"],
            data["correct_answer"],
            data["question"]
        )
    }