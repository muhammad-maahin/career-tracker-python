from fastapi import FastAPI
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
    goals = load_data()
    return goals

@app.post("/goals")
def add_goal(goal: Goal):
    goals = load_data()
    new_goal = {
        "title": goal.title,
        "completed": False
    }
    goals.append(new_goal)
    save_data(goals)
    return {"message": "Goal added", "goal": new_goal}

@app.put("/goals/{id}")
def complete_goal(id: int):
    goals = load_data()
    if 0 <= id - 1 < len(goals):
        goals[id - 1]["completed"] = True
        save_data(goals)
        return {"message": "Goal marked complete"}
    return {"message": "Goal not found"}

@app.delete("/goals/{id}")
def delete_goal(id: int):
    goals = load_data()
    if 0 <= id - 1 < len(goals):
        removed = goals.pop(id - 1)
        save_data(goals)
        return {"message": f"Deleted: {removed['title']}"}
    return {"message": "Goal not found"}