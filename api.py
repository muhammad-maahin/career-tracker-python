from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from storage import load_data, save_data

app = FastAPI()

class Goal(BaseModel):
    title: str


@app.get("/")
def home():
    return {"message": "Career Tracker API is running"}


@app.get("/goals")
def get_goals():
    return load_data()


@app.post("/goals")
def add_goal(goal: Goal):
    goals = load_data()

    new_goal = {
        "id": len(goals) + 1,
        "title": goal.title,
        "completed": False
    }

    goals.append(new_goal)
    save_data(goals)
    return new_goal


@app.put("/goals/{goal_id}")
def mark_complete(goal_id: int):
    goals = load_data()

    for goal in goals:
        if goal["id"] == goal_id:
            goal["completed"] = True
            save_data(goals)
            return goal

    raise HTTPException(status_code=404, detail="Goal not found")


@app.delete("/goals/{goal_id}")
def delete_goal(goal_id: int):
    goals = load_data()

    for i, goal in enumerate(goals):
        if goal["id"] == goal_id:
            removed = goals.pop(i)
            save_data(goals)
            return removed

    raise HTTPException(status_code=404, detail="Goal not found")