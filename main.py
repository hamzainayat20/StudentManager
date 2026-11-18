"""Console app for the Student Task Manager."""

from task_manager import TaskManager


def show_menu():
    print("\nStudent Task Manager")
    print("1. Add task")
    print("2. Display tasks")
    print("3. Complete task")
    print("4. Exit")


def display_tasks(manager):
    tasks = manager.get_tasks()
    if not tasks:
        print("No tasks yet.")
        return
    for task in tasks:
        mark = "done" if task["completed"] else "not done"
        print(f'{task["id"]}. {task["title"]} [{mark}]')


def read_id(prompt):
    try:
        return int(input(prompt).strip())
    except ValueError:
        print("Please enter a valid task number.")
        return None


def main():
    manager = TaskManager()
    while True:
        show_menu()
        choice = input("Choose an option (1-4): ").strip()
        if choice == "1":
            title = input("Enter task title: ")
            try:
                task = manager.add_task(title)
                print(f'Added task {task["id"]}: {task["title"]}')
            except ValueError as e:
                print(e)
        elif choice == "2":
            display_tasks(manager)
        elif choice == "3":
            task_id = read_id("Enter task id to complete: ")
            if task_id is None:
                continue
            try:
                task = manager.complete_task(task_id)
                print(f'Completed task {task["id"]}: {task["title"]}')
            except ValueError as e:
                print(e)
        elif choice == "4":
            print("Goodbye.")
            break
        else:
            print("Please choose 1, 2, 3 or 4.")


if __name__ == "__main__":
    main()
