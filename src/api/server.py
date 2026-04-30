from fastapi import FastAPI

app = FastAPI(title="EduMind Agent API")

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/ask")
def ask(payload: dict):
    question = payload.get("question", "")
    return {"question": question, "answer": "demo answer", "trace_id": "edu-agent-demo"}
