import unittest
from datetime import datetime, timedelta
from src.itemCard import itemCard
from src.tracker import Tracker


class TestTaskManager(unittest.TestCase):

    # Przygotowanie testowych danych przed każdym testem
    def setUp(self):
        self.manager = Tracker()
        self.task1 = itemCard("Zadanie 1")  # nowe, niewykonane
        self.task2 = itemCard("Zadanie 2", due_date=datetime.now() - timedelta(days=1))  # przeterminowane
        self.task3 = itemCard("Zadanie 3")  # wykonane
        self.task3.mark_completed()

    # Test dodania poprawnego zadania
    def test_add_task(self):
        self.manager.add_task(self.task1)
        self.assertIn(self.task1, self.manager.tasks)

    # Test próby dodania niepoprawnego obiektu (np. stringa zamiast itemCard)
    def test_add_invalid_task(self):
        with self.assertRaises(TypeError):
            self.manager.add_task("Nie jestem zadaniem")

    # Test usunięcia zadania z listy
    def test_remove_task(self):
        self.manager.add_task(self.task1)
        self.manager.remove_task(self.task1)
        self.assertNotIn(self.task1, self.manager.tasks)

    # Test usunięcia zadania, które nie istnieje w managerze
    def test_remove_nonexistent_task(self):
        with self.assertRaises(ValueError):
            self.manager.remove_task(self.task1)

    # Test pobrania tylko wykonanych zadań
    def test_get_completed_tasks(self):
        self.manager.add_task(self.task1)
        self.manager.add_task(self.task3)
        completed = self.manager.get_completed_tasks()
        self.assertIn(self.task3, completed)
        self.assertNotIn(self.task1, completed)

    # Test pobrania niewykonanych zadań
    def test_get_uncompleted_tasks(self):
        self.manager.add_task(self.task1)
        self.manager.add_task(self.task3)
        uncompleted = self.manager.get_uncompleted_tasks()
        self.assertIn(self.task1, uncompleted)
        self.assertNotIn(self.task3, uncompleted)

    # Test pobrania tylko zadań przeterminowanych
    def test_get_overdue_tasks(self):
        self.manager.add_task(self.task1)
        self.manager.add_task(self.task2)
        overdue = self.manager.get_overdue_tasks()
        self.assertIn(self.task2, overdue)
        self.assertNotIn(self.task1, overdue)

    # Test wyczyszczenia wszystkich zadań
    def test_clear_all(self):
        self.manager.add_task(self.task1)
        self.manager.add_task(self.task2)
        self.manager.clear_all()
        self.assertEqual(len(self.manager.tasks), 0)

    # Test dodania wielu zadań do listy
    def test_add_multiple_tasks(self):
        tasks = [itemCard(f"Task {i}") for i in range(10)]
        for task in tasks:
            self.manager.add_task(task)
        self.assertEqual(len(self.manager.tasks), 10)

    # Test dodania tego samego zadania więcej niż raz
    def test_duplicate_task_instances(self):
        self.manager.add_task(self.task1)
        self.manager.add_task(self.task1)
        self.assertEqual(self.manager.tasks.count(self.task1), 2)

    # Test działania metod filtrujących, gdy lista zadań jest pusta
    def test_manager_filtering_empty(self):
        self.assertEqual(self.manager.get_completed_tasks(), [])
        self.assertEqual(self.manager.get_uncompleted_tasks(), [])
        self.assertEqual(self.manager.get_overdue_tasks(), [])

    # Test dwukrotnego wyczyszczenia listy zadań (druga próba nie powinna wywołać błędu)
    def test_clear_all_twice(self):
        self.manager.add_task(self.task1)
        self.manager.clear_all()
        self.manager.clear_all()  # ponownie, nie powinien wystąpić błąd
        self.assertEqual(len(self.manager.tasks), 0)



if __name__ == "__main__":
    unittest.main()
