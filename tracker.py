from storage import load_data, save_data
from datetime import datetime

def add_goal():
    goals = load_data()

    title = input("Enter your goal: ")
    goal = {
        "title": title,
        "completed": False,
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M")
    }

    goals.append(goal)
    save_data(goals)
    print("Goal added successfully!")

def view_goals():
    goals = load_data()

    if not goals:
        print("No goals found.")
        return

    print("\n--- Your Goals ---")
    for i, goal in enumerate(goals, 1):
        status = "✔" if goal["completed"] else "✘"
        print(f"{i}. {goal['title']} [{status}] - Added: {goal.get('created_at', 'N/A')}")

def mark_complete():
    goals = load_data()

    view_goals()
    index = int(input("Enter goal number to mark complete: ")) - 1

    if 0 <= index < len(goals):
        goals[index]["completed"] = True
        save_data(goals)
        print("Goal marked as complete!")
    else:
        print("Invalid selection.")

def delete_goal():
    goals = load_data()

    view_goals()
    index = int(input("Enter goal number to delete: ")) - 1

    if 0 <= index < len(goals):
        removed = goals.pop(index)
        save_data(goals)
        print(f"Deleted: {removed['title']}")
    else:
        print("Invalid selection.")

def edit_goal():
    goals = load_data()

    view_goals()
    index = int(input("Enter goal number to edit: ")) - 1

    if 0 <= index < len(goals):
        new_title = input("Enter new goal title: ")
        goals[index]["title"] = new_title
        save_data(goals)
        print("Goal updated successfully!")
    else:
        print("Invalid selection.")