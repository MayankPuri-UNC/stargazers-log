"""A tiny command-line to-do list for practicing Git."""

from utils.storage import load_tasks, save_tasks
from utils.formatting import print_tasks


def main():
    tasks = load_tasks()

    while True:
        print("\n1) View tasks  2) Add task  3) Complete task  4) Quit")
        choice = input("> ").strip()

        if choice == "1":
            print_tasks(tasks)
        elif choice == "2":
            title = input("Task title: ").strip()
            if title:
                tasks.append({"title": title, "done": False})
                save_tasks(tasks)
                print(f"Added: {title}")
        elif choice == "3":
            print_tasks(tasks)
            try:
                index = int(input("Task number: ")) - 1
                tasks[index]["done"] = True
                save_tasks(tasks)
                print("Marked as done!")
            except (ValueError, IndexError):
                print("Invalid task number.")
        elif choice == "4":
            print("Bye!")
            break
        else:
            print("Unknown option.")


if __name__ == "__main__":
    main()
