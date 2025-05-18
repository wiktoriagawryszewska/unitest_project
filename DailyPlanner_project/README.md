# TODO Project (Python) 

Prosty menedżer zadań (lista TODO) napisany w Pythonie. Projekt spełnia wymagania zaliczeniowe z przedmiotu **Programowanie Funkcjonalne i Obiektowe (PFCW)**.

## Struktura projektu


## Jak uruchomić

1. Stwórz środowisko:
    ```bash
    python -m venv .venv
    ```

2. Aktywuj środowisko:
    - Windows: `.\.venv\Scripts\activate`
    - Linux/macOS: `source .venv/bin/activate`

3. Zainstaluj zależności:
    ```bash
    pip install -r requirements.txt
    ```

4. Uruchom testy:
    ```bash
    python -m unittest discover -s tests
    ```

##  Pokrycie kodu

Uruchom testy z `coverage`:
```bash
coverage run -m unittest discover -s tests
coverage report -m

