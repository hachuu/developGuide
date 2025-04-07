# app/main.py
from fastapi import FastAPI
from pydantic import BaseModel
from .rag_engine import generate_answer_from_rag  # rag_engine 함수 임포트

app = FastAPI()

class QuestionRequest(BaseModel):
    question: str

@app.post("/api/ask")
async def ask_question(req: QuestionRequest):
    try:
        answer = generate_answer_from_rag(req.question)
        return {"answer": answer}
    except Exception as e:
        return {"error": str(e)}
