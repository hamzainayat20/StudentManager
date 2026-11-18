"""Console app for the Student Task Manager."""

from task_manager import TaskManager


def show_menu():
    print("\nStudent Task Manager")
    print("1. Add task")
    print("2. Display tasks")
    print("3. Exit")


def display_tasks(manager):
    tasks = manager.get_tasks()
    if not tasks:
        print("No tasks yet.")
        return
    for task in tasks:
        mark = "done" if task["completed"] else "not done"
        print(f'{task["id"]}. {task["title"]} [{mark}]')


def main():
    manager = TaskManager()
    while True:
        show_menu()
        choice = input("Choose an option (1-3): ").strip()
        if choice == "1":
            title = input("Enter task title: ")
            task = manager.add_task(title)
            print(f'Added task {task["id"]}: {task["title"]}')
        elif choice == "2":
            display_tasks(manager)
        elif choice == "3":
            print("Goodbye.")
            break
        else:
            print("Please choose 1, 2 or 3.")


if __name__ == "__main__":
    main()
