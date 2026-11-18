# Student Task Manager

Project status: Active Development

A small Python console app to add, display, complete and delete student tasks. Tasks are saved in `tasks.json`, so they stay there after the app closes.

Author: Hamza Inayat, SP23-BSE-120
Course: CSC418 DevOps for Cloud Computing, Lab Assignment 4

## Features

- Add a task, with empty titles rejected
- Display all tasks, showing which ones are done
- Mark a task complete using its task id
- Delete a task using its task id
- Tasks are saved to a JSON file

## Setup

You need Python 3.10 or newer. No extra packages are needed.

```bash
git clone https://github.com/hamzainayat20/StudentManager.git
cd StudentManager
```


## Usage

Run the app with:

```bash
python main.py
```

Then use the menu:

```text
1. Add task
2. Display tasks
3. Complete task
4. Delete task
5. Exit
```

Add a task by typing a title. Complete or delete a task by typing its id number, shown in the task list. An id that does not exist is rejected with a clear message.

## Test instructions

Run the tests with:

```bash
python -m unittest discover -s tests -v
```

There are six tests. They cover adding a task, rejecting an empty title, marking a task complete, rejecting an invalid id for completing, deleting a task, and rejecting an invalid id for deleting.

Tests also run automatically on GitHub Actions, on every push to `main` and on every pull request to `main`. See `.github/workflows/tests.yml`.

## Project layout

```text
main.py                  Console menu, uses TaskManager
task_manager.py          TaskManager class, add, list, complete, delete
tests/test_task_manager.py  Unit tests with Python unittest
docs/userguide.md        Short user guide
LABREPORT.md             Assignment report, answers in my own words
```

## License

MIT License. See `LICENSE`.
