# Career Tracker (Python)

A command-line based career tracking application built with Python.

## Features

- Add goals
- View goals
- Mark goals complete
- Edit goals
- Delete goals
- Persistent storage using JSON
- Timestamp tracking

## Tech Used

- Python
- JSON (File storage)

## How to Run

```bash
python main.py
```

## Project Structure

- main.py → entry point
- tracker.py → logic
- storage.py → data handling
- data.json → storage

## API Endpoints

GET /goals - Get all goals
POST /goals - Add a new goal
PUT /goals/{id} - Mark goal as complete
DELETE /goals/{id} - Delete a goal

Built using FastAPI.

## Author

Muhammad Maahin
