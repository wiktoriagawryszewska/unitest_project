# Daily Planner (Python)

A simple task management application written in Python.  
The project was created as part of the **Functional and Object-Oriented Programming (PFCW)** course.

The application allows users to create, manage, and store tasks, and includes **unit tests implemented using Python's built-in `unittest` framework**.

---

## Features

- Create and manage tasks
- Save and load data from JSON files
- Simple and modular architecture
- Unit testing with `unittest`

---

## Project Structure

- `src/itemCard.py` – task model (class definition)
- `src/tracker.py` – task manager (add, remove, filter tasks)
- `src/supportBox.py` – data persistence (JSON handling)
- `tests/` – unit tests for core functionalities

---

## Getting Started

### 1. Create virtual environment

```bash
python -m venv .venv
```

### 2. Activate environment

- Windows:
```bash
.\.venv\Scripts\activate
```

- macOS / Linux:
```bash
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## Running Tests

The project uses Python's built-in `unittest` framework.

Run all tests:

```bash
python -m unittest discover -s tests
```

---

## Test Coverage

To check code coverage, use:

```bash
coverage run -m unittest discover -s tests
coverage report -m
```

---

## Technologies

- Python
- unittest
- JSON
- Git

---

## Purpose

This project demonstrates:
- object-oriented programming principles
- basic data management
- writing and executing unit tests
- project structure organization

---

## Author

Wiktoria Gawryszewska
