import requests

BASE = "http://127.0.0.1:8000"

# Test 1 - Add goals
print("--- Adding Goals ---")
r = requests.post(f"{BASE}/goals", json={"title": "Learn FastAPI"})
print(r.json())

r = requests.post(f"{BASE}/goals", json={"title": "Build Portfolio"})
print(r.json())

# Test 2 - View all goals
print("\n--- All Goals ---")
r = requests.get(f"{BASE}/goals")
print(r.json())

# Test 3 - Mark complete
print("\n--- Mark Goal 1 Complete ---")
r = requests.put(f"{BASE}/goals/1")
print(r.json())

# Test 4 - Delete goal
print("\n--- Delete Goal 2 ---")
r = requests.delete(f"{BASE}/goals/2")
print(r.json())

# Test 5 - View final state
print("\n--- Final Goals ---")
r = requests.get(f"{BASE}/goals")
print(r.json())