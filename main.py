from fastapi import FastAPI
from pydantic import BaseModel

from rag.retriever import search
from rag.generator import generate_answer

app = FastAPI()

class Query(BaseModel):
    query: str

@app.post("/ai-trip")
def ai_trip(q: Query):

    docs = search(q.query)

    context = "\n".join([
        d.page_content for d in docs
    ])

    answer = generate_answer(context, q.query)

    return {
        "response": answer
    }