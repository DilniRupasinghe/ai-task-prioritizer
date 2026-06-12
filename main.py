from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Request format
class TaskRequest(BaseModel):
    tasks: List[str]

@app.get("/")
def home():
    return {"message": "AI Task Prioritizer API is running"}

@app.post("/prioritize")
def prioritize_tasks(request: TaskRequest):
    tasks = request.tasks

    # Simple dummy logic first (NO AI yet)
    sorted_tasks = sorted(tasks, key=len, reverse=True)

    return {
        "original_tasks": tasks,
        "prioritized_tasks": sorted_tasks,
        "note": "This is placeholder logic (no AI yet)"
    }