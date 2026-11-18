# Student Task Manager User Guide

## What this app does

This app keeps a simple list of your study tasks. You can add a task, see all your tasks, mark one as done, and delete one you no longer need.

## Starting the app

Make sure Python 3.10 or newer is installed, then run:

```bash
python main.py
```

## Adding a task

1. Choose option 1, Add task.
2. Type the task title and press Enter.
3. The app shows the new task number, for example `Added task 1: Finish CSC418 lab`.

A title with only spaces is not accepted. The app tells you the title cannot be empty, and asks you to try again.

## Seeing your tasks

Choose option 2, Display tasks. Each task is shown with its number, its title, and whether it is done or not done, for example:

```text
1. Finish CSC418 lab [not done]
1. Finish CSC418 lab [done]
```

If there are no tasks, the app says `No tasks yet.`

## Completing a task

1. Choose option 3, Complete task.
2. Type the task number shown in the list.
3. The app marks that task as done.

If you type a number that does not match any task, the app says no task was found with that id.

## Deleting a task

1. Choose option 4, Delete task.
2. Type the task number shown in the list.
3. The app deletes that task.

If you type a number that does not match any task, the app says no task was found with that id, and nothing is deleted.

## Where tasks are saved

Tasks are saved in `tasks.json` in the same folder as the app. If you delete that file, your task list starts empty again.

## Leaving the app

Choose option 5, Exit. Your tasks are already saved, so you can close the app at any time after a task is added, completed or deleted.
