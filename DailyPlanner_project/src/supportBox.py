import json
from datetime import datetime
from src.itemCard import itemCard


# Zamienia obiekt itemCard na słownik (do zapisu w pliku JSON).
def task_to_dict(task: itemCard) -> dict:
    return {
        "title": task.title,
        "description": task.description,
        "due_date": task.due_date.isoformat() if task.due_date else None,
        "completed": task.completed,
        "created_at": task.created_at.isoformat()
    }

# Tworzy obiekt itemCard na podstawie danych ze słownika (np. wczytanych z pliku).
def task_from_dict(data: dict) -> itemCard:
    task = itemCard(
        title=data["title"],
        description=data.get("description", ""),
        due_date=datetime.fromisoformat(data["due_date"]) if data["due_date"] else None
    )
    if data["completed"]:
        task.mark_completed()
    return task

# Zapisuje listę zadań do pliku .
def save_tasks_to_file(tasks: list[itemCard], filename: str):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump([task_to_dict(t) for t in tasks], f, indent=2)

# Wczytuje listę zadań z pliku i konwertuje je na obiekty itemCard.
def load_tasks_from_file(filename: str) -> list[itemCard]:
    with open(filename, "r", encoding="utf-8") as f:
        data = json.load(f)
        return [task_from_dict(d) for d in data]