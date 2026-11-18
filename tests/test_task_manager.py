"""Tests for the Student Task Manager, using Python unittest."""

import os
import tempfile
import unittest

from task_manager import TaskManager


class TestTaskManager(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.storage = os.path.join(self.tmp.name, "tasks.json")
        self.manager = TaskManager(storage=self.storage)

    def tearDown(self):
        self.tmp.cleanup()

    def test_add_task(self):
        task = self.manager.add_task("Finish CSC418 lab")
        self.assertEqual(task["title"], "Finish CSC418 lab")
        self.assertFalse(task["completed"])
        self.assertEqual(len(self.manager.get_tasks()), 1)

    def test_add_task_rejects_empty_title(self):
        with self.assertRaises(ValueError):
            self.manager.add_task("")
        with self.assertRaises(ValueError):
            self.manager.add_task("   ")

    def test_list_tasks(self):
        self.manager.add_task("Read chapter 3")
        self.manager.add_task("Buy notebook")
        self.assertEqual(len(self.manager.get_tasks()), 2)


if __name__ == "__main__":
    unittest.main()
