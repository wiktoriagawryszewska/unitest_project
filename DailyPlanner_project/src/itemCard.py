from datetime import datetime

class itemCard:
    # Tworzy nowe zadanie z tytułem, opcjonalnym opisem i terminem.
    # Sprawdza poprawność tytułu i konwertuje datę, jeśli podano ją jako tekst.
    def __init__(self, title, description="", due_date=None):
        if not title or not title.strip():
            raise ValueError("Task title cannot be empty.")
        self.title = title.strip()
        self.description = description.strip()

        if isinstance(due_date, str):
            try:
                due_date = datetime.fromisoformat(due_date)
            except ValueError:
                raise ValueError("Invalid date format. Use YYYY-MM-DD")

        self.due_date = due_date
        self.completed = False
        self.created_at = datetime.now()

    # Sprawdza, czy tytuł zadania jest poprawny (od 2 do 20 znaków).
    def _validate_title(self):
        if not isinstance(self.title, str):
            return False
        if len(self.title.strip()) < 2 or len(self.title.strip()) > 20:
            return False
        return True

    # Ustawia zadanie jako wykonane.
    def mark_completed(self):
        self.completed = True

    # Ustawia zadanie jako niewykonane.
    def mark_uncompleted(self):
        self.completed = False

    # Sprawdza, czy zadanie jest po terminie (czy jest przeterminowane).
    def is_overdue(self):
        if self.due_date is None:
            return False
        return datetime.now() > self.due_date

    # Zwraca tekstową reprezentację zadania, np. [✓] Zakupy (2025-05-18)
    def __str__(self):
        status = "✓" if self.completed else "✗"
        return f"[{status}] {self.title} ({self.created_at.strftime('%Y-%m-%d')})"
