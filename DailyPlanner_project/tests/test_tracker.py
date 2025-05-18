import unittest
import os
from datetime import datetime, timedelta
from src.itemCard import itemCard
from src.supportBox import save_tasks_to_file, load_tasks_from_file


class TestTracker(unittest.TestCase):

    # Przygotowanie przykładowego zadania i pliku testowego przed każdym testem
    def setUp(self):
        self.task = itemCard(
            title="Testowe zadanie",
            description="Opis zadania",
            due_date=datetime.now() + timedelta(days=1)
        )
        self.task.mark_completed()
        self.filename = "test_tasks.json"

    # Usunięcie pliku testowego po każdym teście (żeby nie zostawał na dysku)
    def tearDown(self):
        if os.path.exists(self.filename):
            os.remove(self.filename)

    # Test zapisu pojedynczego zadania do pliku i jego poprawnego odczytu
    def test_save_and_load_tasks(self):
        save_tasks_to_file([self.task], self.filename)
        loaded_tasks = load_tasks_from_file(self.filename)

        self.assertEqual(len(loaded_tasks), 1)
        loaded = loaded_tasks[0]
        self.assertEqual(loaded.title, self.task.title)
        self.assertEqual(loaded.description, self.task.description)
        self.assertEqual(loaded.completed, self.task.completed)
        self.assertEqual(loaded.due_date.date(), self.task.due_date.date())  # tylko data (bez czasu)

    # Test zapisu wielu zadań do pliku i sprawdzenia, czy wszystkie zostały wczytane
    def test_save_multiple_tasks(self):
        tasks = [
            itemCard("Task A", description="X"),
            itemCard("Task B", due_date=datetime.now() + timedelta(days=3)),
            itemCard("Task C")
        ]
        save_tasks_to_file(tasks, self.filename)
        loaded = load_tasks_from_file(self.filename)
        self.assertEqual(len(loaded), 3)

    # Test zapisu pustej listy zadań i sprawdzenia, czy odczytana lista też jest pusta
    def test_save_empty_list(self):
        save_tasks_to_file([], self.filename)
        loaded = load_tasks_from_file(self.filename)
        self.assertEqual(loaded, [])


if __name__ == "__main__":
    unittest.main()
