from src.itemCard import itemCard
from typing import List

class Tracker:
    # Inicjalizuje menedżera zadań z pustą listą.
    def __init__(self):
        self.tasks: List[itemCard] = []

    # Dodaje nowe zadanie do listy (musi być typu itemCard).
    def add_task(self, task: itemCard):
        if not isinstance(task, itemCard):
            raise TypeError("Can only add Task instances.")
        self.tasks.append(task)

    # Usuwa konkretne zadanie z listy.
    def remove_task(self, task: itemCard):
        if task not in self.tasks:
            raise ValueError("Task not found.")
        self.tasks.remove(task)

    # Zwraca listę zadań oznaczonych jako wykonane.
    def get_completed_tasks(self) -> List[itemCard]:
        return [task for task in self.tasks if task.completed]

    # Zwraca listę zadań, które jeszcze nie zostały ukończone.
    def get_uncompleted_tasks(self) -> List[itemCard]:
        return [task for task in self.tasks if not task.completed]

    # Zwraca listę zadań, których termin już minął.
    def get_overdue_tasks(self) -> List[itemCard]:
        return [task for task in self.tasks if task.is_overdue()]

    # Czyści całą listę zadań.
    def clear_all(self):
        self.tasks.clear()
