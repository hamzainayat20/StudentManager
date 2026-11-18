"""Student Task Manager: simple task list with file storage."""

import json
import os


class TaskManager:
    """Keep a list of tasks, saved as JSON so work is not lost."""

    def __init__(self, storage="tasks.json"):
        self.storage = storage
        self.tasks = []
        self.next_id = 1
        self.load()

    def load(self):
        if not os.path.exists(self.storage):
            return
        try:
            with open(self.storage, "r", encoding="utf-8") as f:
                data = json.load(f)
        except (json.JSONDecodeError, OSError):
            data = []
        self.tasks = data
        if self.tasks:
            self.next_id = max(t["id"] for t in self.tasks) + 1

    def save(self):
        with open(self.storage, "w", encoding="utf-8") as f:
            json.dump(self.tasks, f, indent=2)

    def add_task(self, title):
        """Add a task."""
        task = {"id": self.next_id, "title": str(title).strip(), "completed": False}
        self.next_id += 1
        self.tasks.append(task)
        self.save()
        return task

    def get_tasks(self):
        return list(self.tasks)
