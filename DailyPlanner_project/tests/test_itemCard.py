import unittest
from datetime import datetime, timedelta
from src.itemCard import itemCard


class TestItemCard(unittest.TestCase):

    # Sprawdza, czy konstruktor wykrywa pusty tytuł i błędny format daty
    def test_initialization_failurer(self):
        with self.assertRaises(ValueError) as context:
            itemCard(
                title="   ",
                description="Opis zadania",
                due_date="2025/07/06"  # błędny format (powinno być YYYY-MM-DD)
            )
        self.assertIn("Task title cannot be empty", str(context.exception))

    # Sprawdza różne błędne tytuły: liczby, za krótkie, za długie, puste
    def test_validate_title(self):
        titles = [123, "c", "", "title" * 10]
        for title in titles:
            with self.subTest(title=title):
                task = itemCard("Dummy")
                task.title = title
                self.assertFalse(task._validate_title())

    # Poprawna inicjalizacja zadania – wszystkie wartości domyślne i niestandardowe
    def test_task_creation_valid(self):
        task = itemCard("Zrobić projekt", "Na przedmiot PF")
        self.assertEqual(task.title, "Zrobić projekt")
        self.assertFalse(task.completed)
        self.assertIsNotNone(task.created_at)

    # Konstruktor powinien odrzucić pusty tytuł
    def test_task_title_empty(self):
        with self.assertRaises(ValueError):
            itemCard("   ")

    # Oznaczanie zadania jako ukończone
    def test_mark_completed(self):
        task = itemCard("Zrobić zakupy")
        task.mark_completed()
        self.assertTrue(task.completed)

    # Cofanie oznaczenia wykonania zadania
    def test_mark_uncompleted(self):
        task = itemCard("Posprzątać pokój")
        task.mark_completed()
        task.mark_uncompleted()
        self.assertFalse(task.completed)

    # Zadanie z przeszłą datą – powinno być przeterminowane
    def test_is_overdue_true(self):
        overdue_task = itemCard("Stare zadanie", due_date="2025-05-13")
        self.assertTrue(overdue_task.is_overdue())

    # Zadanie z przyszłą datą – nie powinno być przeterminowane
    def test_is_overdue_false(self):
        upcoming_task = itemCard("Nowe zadanie", due_date="2025-07-20")
        self.assertFalse(upcoming_task.is_overdue())

    # Reprezentacja tekstowa zadania zawiera tytuł i symbol statusu
    def test_str_representation(self):
        task = itemCard("Testowe zadanie")
        result = str(task)
        self.assertIn(task.title, result)
        self.assertTrue("✓" in result or "✗" in result)

    # Wiele różnych błędnych tytułów – powinny powodować wyjątek
    def test_invalid_titles_multiple(self):
        invalid_titles = ["", " ", "\n", "\t"]
        for title in invalid_titles:
            with self.subTest(title=title):
                with self.assertRaises(ValueError):
                    itemCard(title)

    # Sprawdza symbole ✓ i ✗ w zależności od stanu zadania
    def test_str_representation_symbols(self):
        task1 = itemCard("Zadanie 1")
        task2 = itemCard("Zadanie 2")
        task2.mark_completed()
        self.assertIn("✗", str(task1))
        self.assertIn("✓", str(task2))

    # Sprawdza, czy bardzo długi opis jest zapisywany poprawnie
    def test_task_with_long_description(self):
        description = "a" * 1000
        task = itemCard("Tytuł", description=description)
        self.assertEqual(task.description, description)

    # Czy format daty jest poprawnie przypisany
    def test_due_date_format(self):
        date = datetime(2025, 5, 10, 12, 0)
        task = itemCard("Zadanie", due_date=date)
        self.assertEqual(task.due_date, date)

    # Czy `created_at` jest obiektem typu datetime
    def test_created_at_is_datetime(self):
        task = itemCard("Zadanie")
        self.assertIsInstance(task.created_at, datetime)

    # Test stworzenia obiektu i sprawdzenia daty utworzenia
    def test_created_at_type_25(self):
        task = itemCard("Zadanie 25")
        self.assertIsInstance(task.created_at, datetime)

    # Test opisu zawierającego słowo "testowy"
    def test_description_assignment_26(self):
        task = itemCard("Zadanie 26", description="Opis testowy 26")
        self.assertIn("testowy", task.description)

    # Tytuł składający się tylko ze spacji – powinien być błędem
    def test_invalid_title_27(self):
        with self.assertRaises(ValueError):
            itemCard(" ")

    # Tytuł z dodatkowymi spacjami powinien zostać przycięty
    def test_trimmed_title_28(self):
        task = itemCard("  Zadanie 28  ")
        self.assertEqual(task.title, "Zadanie 28")

    # Zadanie z datą w przyszłości nie powinno być uznane za przeterminowane
    def test_due_date_future_29(self):
        task = itemCard("Zadanie 29", due_date="2025-07-06")
        self.assertFalse(task.is_overdue())

    # Zadanie z datą w przeszłości powinno być uznane za przeterminowane
    def test_due_date_past_30(self):
        task = itemCard("Zadanie 30", due_date="2025-04-13")
        self.assertTrue(task.is_overdue())

    # Po oznaczeniu zadania jako ukończone, jego status powinien być zmieniony
    def test_task_completed_status_31(self):
        task = itemCard("Zadanie 31")
        task.mark_completed()
        self.assertTrue(task.completed)

    # Sprawdza, czy `created_at` to obiekt typu datetime
    def test_created_at_type_32(self):
        task = itemCard("Zadanie 32")
        self.assertIsInstance(task.created_at, datetime)

    # Sprawdza, czy opis zadania został poprawnie przypisany
    def test_description_assignment_33(self):
        task = itemCard("Zadanie 33", description="Opis testowy 33")
        self.assertIn("testowy", task.description)

    # Zadanie z pustym tytułem powinno rzucić wyjątek
    def test_invalid_title_34(self):
        with self.assertRaises(ValueError):
            itemCard(" ")

    # Sprawdza, czy tytuł zawiera określony tekst (słowo kluczowe)
    def test_title_contains_text_35(self):
        task = itemCard("Projekt PFCW")
        self.assertIn("PFCW", task.title)

    # Sprawdza, czy termin wykonania zadania zgadza się z ustawionym datetime
    def test_due_date_exact_match_36(self):
        due = datetime(2025, 6, 1)
        task = itemCard("Termin zadania", due_date=due)
        self.assertEqual(task.due_date, due)

    # Po utworzeniu nowego zadania, jego status nie powinien być oznaczony jako ukończony
    def test_task_not_completed_initially_37(self):
        task = itemCard("Zadanie domyślne")
        self.assertFalse(task.completed)

    # Sprawdza, czy oznaczenie zadania jako ukończone działa poprawnie
    def test_mark_completed_changes_status_38(self):
        task = itemCard("Zrobić prezentację")
        task.mark_completed()
        self.assertTrue(task.completed)

    # Sprawdza, czy data utworzenia zadania została przypisana bardzo niedawno (do 5 sekund różnicy)
    def test_created_at_is_recent_39(self):
        task = itemCard("Zadanie nowe")
        now = datetime.now()
        self.assertLess(abs((now - task.created_at).total_seconds()), 5)

    # Sprawdza, czy opis zawiera odpowiednią długość tekstu (przynajmniej 10 znaków)
    def test_description_length_check_40(self):
        task = itemCard("Opisowy test", description="Opis testowy 40")
        self.assertGreaterEqual(len(task.description), 10)

    # Sprawdza, czy tytuł można poprawnie zamienić na wielkie litery
    def test_title_uppercase_41(self):
        task = itemCard("zadanie 41")
        self.assertEqual(task.title.upper(), "ZADANIE 41")

    # Sprawdza, czy zadana data wykonania faktycznie znajduje się w przyszłości
    def test_due_date_is_in_future_42(self):
        task = itemCard("Zadanie 42", due_date=datetime.now() + timedelta(days=10))
        self.assertGreater(task.due_date, datetime.now())

    # Sprawdza, czy opis zaczyna się od określonego słowa (np. "Ważne")
    def test_description_startswith_word_43(self):
        task = itemCard("Zadanie 43", description="Ważne: zrobić coś")
        self.assertTrue(task.description.startswith("Ważne"))

    # Sprawdza, czy tekstowa reprezentacja zadania zawiera symbol ✗
    def test_string_representation_symbol_44(self):
        task = itemCard("Zadanie 44")
        self.assertIn("✗", str(task))

    # Sprawdza, czy status zmienia się po oznaczeniu jako ukończone
    def test_mark_and_check_completed_state_45(self):
        task = itemCard("Zadanie 45")
        self.assertFalse(task.completed)
        task.mark_completed()
        self.assertTrue(task.completed)

    # Sprawdza, czy `created_at` wskazuje czas bliski obecnemu (do 2 sekund różnicy)
    def test_created_at_is_recent_46(self):
        task = itemCard("Zadanie 46")
        seconds_diff = abs((datetime.now() - task.created_at).total_seconds())
        self.assertLess(seconds_diff, 2)

    # Zadanie z przeszłą datą powinno być uznane za przeterminowane
    def test_setting_due_date_in_past_and_check_overdue_47(self):
        past = datetime.now() - timedelta(days=10)
        task = itemCard("Zadanie 47", due_date=past)
        self.assertTrue(task.is_overdue())

    # Sprawdza, że tytuł nie składa się wyłącznie z cyfr
    def test_title_is_not_numeric_48(self):
        task = itemCard("Zadanie48")
        self.assertFalse(task.title.isnumeric())

    # Sprawdza, czy dzień z daty wykonania zgadza się z oczekiwanym dniem
    def test_due_date_exact_day_comparison_49(self):
        date = datetime(2025, 5, 25, 14, 30)
        task = itemCard("Zadanie 49", due_date=date)
        self.assertEqual(task.due_date.day, 25)

    # Sprawdza, czy domyślnie opis zadania jest pusty
    def test_task_has_no_description_by_default_50(self):
        task = itemCard("Zadanie 50")
        self.assertEqual(task.description, "")

    # Sprawdza, czy symbol statusu (✓ lub ✗) znajduje się w opisie zadania
    def test_str_output_contains_status_symbol_51(self):
        task = itemCard("Zadanie 51")
        output = str(task)
        self.assertTrue("✗" in output or "✓" in output)

    # Sprawdza, czy długość tytułu jest większa niż 5 znaków
    def test_title_length_is_reasonable_52(self):
        task = itemCard("Zadanie 52")
        self.assertGreater(len(task.title), 5)

    # Sprawdza, czy oznaczenie jako wykonane wpływa na tekstową reprezentację zadania
    def test_mark_completed_affects_str_output_53(self):
        task = itemCard("Zadanie 53")
        task.mark_completed()
        self.assertIn("✓", str(task))

    # Sprawdza, czy czas utworzenia zadania nie jest w przyszłości
    def test_created_at_is_less_than_now_54(self):
        task = itemCard("Zadanie 54")
        self.assertLessEqual(task.created_at, datetime.now())

    # Sprawdza, czy tytuł może zawierać znak #
    def test_title_contains_hashtag_55(self):
        self.assertIn("#", itemCard("#Zadanie 55").title)

    # Sprawdza, czy opis może być wieloliniowy (zawiera znak nowej linii)
    def test_description_multiline_56(self):
        self.assertIn("\n", itemCard("Zadanie", description="Linia 1\nLinia 2").description)

    # Sprawdza, czy domyślnie generowana reprezentacja zawiera symbol ✗
    def test_str_includes_check_symbol_57(self):
        self.assertIn("✗", str(itemCard("Zadanie 57")))

    # Sprawdza, czy zadanie wykonane dziś, ale późnym wieczorem, nie jest przeterminowane
    def test_task_today_due_is_not_overdue_58(self):
        due_today_late = datetime.now().replace(hour=23, minute=59, second=59, microsecond=0)
        self.assertFalse(itemCard("Zadanie", due_date=due_today_late).is_overdue())

    # Sprawdza, czy dwie różne instancje mają różny czas utworzenia
    def test_unique_created_at_59(self):
        self.assertNotEqual(itemCard("A").created_at, itemCard("B").created_at)

    # Sprawdza, czy tytuł zawierający tabulatory i spacje jest odpowiednio przycięty
    def test_trim_tabs_and_spaces_60(self):
        self.assertEqual(itemCard(" \tZadanie\t ").title, "Zadanie")

    # Sprawdza, czy opis zawiera słowo "PRIORYTET"
    def test_description_priority_keyword_61(self):
        self.assertIn("PRIORYTET", itemCard("Zadanie", description="PRIORYTET – ważne!").description)

    # Sprawdza, czy tytuł zawiera słowo "analiza"
    def test_title_contains_keyword_62(self):
        task = itemCard("Zadanie 62 – analiza danych")
        self.assertIn("analiza", task.title)

    # Sprawdza, czy tytuł zawiera znaki Unicode (np. "ł")
    def test_title_with_unicode_characters_63(self):
        self.assertIn("ł", itemCard("Zadanie 63 – język łaciński").title)

    # Sprawdza, czy dzień ustawionej daty przypada w weekend (sobota – 5)
    def test_due_date_on_weekend_64(self):
        task = itemCard("Zadanie", due_date=datetime(2025, 6, 14))  # sobota
        self.assertEqual(task.due_date.weekday(), 5)

    # Sprawdza, czy zadanie z datą dokładnie o północy dzień wcześniej jest przeterminowane
    def test_overdue_task_with_exact_midnight_65(self):
        date = datetime.now() - timedelta(days=1)
        task = itemCard("Zadanie", due_date=date.replace(hour=0, minute=0))
        self.assertTrue(task.is_overdue())

    # Sprawdza, czy wielokrotne oznaczenie jako wykonane nie zmienia stanu
    def test_mark_completed_twice_66(self):
        task = itemCard("Zadanie")
        task.mark_completed()
        task.mark_completed()
        self.assertTrue(task.completed)

    # Sprawdza, czy zadanie zostało utworzone dzisiaj (data bez godziny)
    def test_created_at_is_today_67(self):
        self.assertEqual(itemCard("Zadanie").created_at.date(), datetime.now().date())

    # Sprawdza, czy opis kończy się wykrzyknikiem
    def test_description_with_exclamation_68(self):
        task = itemCard("Zadanie", description="Uwaga!")
        self.assertTrue(task.description.endswith("!"))

    # Sprawdza, czy w tytule występuje dwukropek (np. do formatowania)
    def test_title_with_colon_and_dash_69(self):
        self.assertIn(":", itemCard("Zadanie 69: test").title)

    # Sprawdza, czy tytuł z twardymi spacjami (non-breaking space) zostanie przycięty poprawnie
    def test_trimmed_title_with_nonbreaking_space_70(self):
        task = itemCard(" Zadanie 70 ")  # zawiera twarde spacje (U+00A0)
        self.assertEqual(task.title.replace('\xa0', ' ').strip(), "Zadanie 70")

    # Sprawdza, czy zadanie może mieć termin w roku przestępnym – 29 lutego
    def test_due_date_on_leap_year_day_71(self):
        leap_day = datetime(2024, 2, 29)
        task = itemCard("Zadanie specjalne", due_date=leap_day)
        self.assertEqual(task.due_date.day, 29)

    # Sprawdza, czy zadanie z datą w przyszłości (o 23:59 jutro) nie jest przeterminowane
    def test_task_not_overdue_for_future_hour_72(self):
        future = datetime.now().replace(hour=23, minute=59) + timedelta(days=1)
        self.assertFalse(itemCard("Zadanie", due_date=future).is_overdue())

    # Sprawdza, czy zakończone zadanie zawiera symbol ✓ w reprezentacji tekstowej
    def test_completed_task_str_has_checkmark_73(self):
        task = itemCard("Zadanie 73")
        task.mark_completed()
        self.assertTrue("✓" in str(task))

    # Sprawdza, czy miesiąc daty utworzenia odpowiada bieżącemu miesiącowi
    def test_created_at_includes_correct_month_74(self):
        task = itemCard("Zadanie 74")
        self.assertEqual(task.created_at.month, datetime.now().month)

    # Sprawdza, czy opis zawiera adres e-mail (czy zawiera znak @)
    def test_description_mentions_email_75(self):
        task = itemCard("Zadanie", description="Wyślij na maila: test@example.com")
        self.assertIn("@", task.description)

    # Sprawdza, czy tytuł przypomina przypomnienie o spotkaniu
    def test_title_for_meeting_reminder_76(self):
        task = itemCard("Spotkanie z klientem")
        self.assertIn("Spotkanie", task.title)

    # Sprawdza, czy opis zawiera element z listy zakupów
    def test_description_for_grocery_list_77(self):
        task = itemCard("Zakupy", description="mleko, chleb, masło")
        self.assertIn("chleb", task.description)

    # Sprawdza, czy zadanie ma datę w weekend (sobota = 5)
    def test_task_with_weekend_due_date_78(self):
        weekend = datetime(2025, 5, 17)  # Sobota
        task = itemCard("Wypoczynek", due_date=weekend)
        self.assertEqual(task.due_date.weekday(), 5)

    # Sprawdza, czy tytuł zawiera znak zapytania (np. pytanie)
    def test_title_contains_question_mark_79(self):
        task = itemCard("Zadanie 86 – gotowe?")
        self.assertIn("?", task.title)

    # Sprawdza, czy oznaczenie zadania jako wykonane działa po treningu
    def test_mark_task_done_after_workout_80(self):
        task = itemCard("Trening poranny")
        task.mark_completed()
        self.assertTrue(task.completed)

    # Sprawdza, czy opis zadania zawiera słowo „maila”
    def test_task_description_for_email_draft_81(self):
        desc = "Wersja robocza maila do szefa"
        task = itemCard("Mail", description=desc)
        self.assertIn("maila", task.description)

    # Sprawdza, czy tytuł nie przekracza maksymalnej długości (20 znaków)
    def test_task_title_is_short_82(self):
        task = itemCard("Zadanie")
        self.assertLessEqual(len(task.title), 20)

    # Sprawdza, czy tytuł przypomina przypomnienie o telefonie
    def test_title_for_call_reminder_83(self):
        task = itemCard("Zadzwonić do Ani")
        self.assertTrue("Zadzwonić" in task.title)

    # Sprawdza, czy tytuł z wieloma spacjami jest poprawnie przycięty
    def test_title_trim_with_multiple_spaces_84(self):
        task = itemCard("   Sprawdzić maila   ")
        self.assertEqual(task.title, "Sprawdzić maila")

    # Sprawdza, czy data zadania przypada w weekend
    def test_due_date_set_for_weekend_85(self):
        weekend_date = datetime(2025, 5, 17)  # Sobota
        task = itemCard("Zadanie weekendowe", due_date=weekend_date)
        self.assertEqual(task.due_date.weekday(), 5)

    # Sprawdza, czy zadanie z datą o północy dnia poprzedniego jest przeterminowane
    def test_due_yesterday_midnight_86(self):
        yesterday = datetime.now() - timedelta(days=1)
        task = itemCard("Zadanie 86", due_date=yesterday.replace(hour=0, minute=0))
        self.assertTrue(task.is_overdue())

    # Sprawdza, czy zmiana stanu na ukończone i cofnięcie działa poprawnie
    def test_toggle_completion_status_twice_87(self):
        task = itemCard("Zadanie 87")
        task.mark_completed()
        task.mark_uncompleted()
        task.mark_completed()
        self.assertTrue(task.completed)

    # Sprawdza, czy data utworzenia ma ten sam dzień co bieżący
    def test_created_at_day_matches_now_88(self):
        task = itemCard("Zadanie 88")
        self.assertEqual(task.created_at.day, datetime.now().day)

    # Sprawdza, czy opis zawiera numer telefonu w formacie xxx-xxx-xxx
    def test_description_contains_phone_number_89(self):
        task = itemCard("Zadanie 89", description="Zadzwoń pod 123-456-789")
        self.assertRegex(task.description, r"\d{3}-\d{3}-\d{3}")

    # Sprawdza, czy tytuł zawiera godzinę (np. przypomnienie z czasem)
    def test_title_with_time_info_90(self):
        task = itemCard("Zadzwonić o 16:00")
        self.assertIn("16:00", task.title)

    # Sprawdza, czy opis zawiera link (np. do strony internetowej)
    def test_description_contains_url_91(self):
        task = itemCard("Zadanie", description="Link: http://szkola.pl/test")
        self.assertTrue("http" in task.description)

    # Sprawdza, czy tytuł zawiera słowo związane z pracą domową
    def test_title_for_school_homework_92(self):
        task = itemCard("Zadanie z matematyki")
        self.assertIn("matematyki", task.title)

    # Sprawdza, czy opis jest zapisany w formie listy kroków (wielolinijkowy)
    def test_description_as_step_list_93(self):
        task = itemCard("Poranek", description="1. Obudzić się\n2. Zjeść śniadanie")
        self.assertIn("\n", task.description)

    # Sprawdza, czy godzina w polu due_date została poprawnie przypisana
    def test_due_date_hour_check_94(self):
        time = datetime.now().replace(hour=22, minute=0)
        task = itemCard("Zadanie nocne", due_date=time)
        self.assertEqual(task.due_date.hour, 22)

    # Sprawdza, czy tytuł został zapisany wielkimi literami
    def test_title_all_uppercase_95(self):
        task = itemCard("PRZYGOTOWAĆ PREZENTACJĘ")
        self.assertTrue(task.title.isupper())

    # Sprawdza, czy opis zawiera słowo „notatki” – wskazujące na zadanie szkolne
    def test_description_contains_task_info_96(self):
        task = itemCard("Zadanie 96", description="Przygotuj notatki do lekcji biologii")
        self.assertIn("notatki", task.description)

    # Sprawdza, czy pusta nazwa zadania (np. same spacje) powoduje wyjątek
    def test_title_blank_raises_error_97(self):
        with self.assertRaises(ValueError):
            itemCard(" ")

    # Sprawdza, czy tytuł z nadmiarowymi spacjami zostaje poprawnie przycięty
    def test_title_is_trimmed_correctly_98(self):
        task = itemCard("   Wysłać CV   ")
        self.assertEqual(task.title, "Wysłać CV")

    # Sprawdza, czy zadanie z terminem na jutro nie jest jeszcze przeterminowane
    def test_task_due_tomorrow_is_not_overdue_99(self):
        task = itemCard("Zadanie", due_date=datetime.now() + timedelta(days=1))
        self.assertFalse(task.is_overdue())


if __name__ == "__main__":
    unittest.main()
