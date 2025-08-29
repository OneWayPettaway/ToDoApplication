def display_menu():
    print("\n=== TO-DO APPLICATION ===")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Quit the application")


def add_task(task_list):
    task = input("Enter a new task: ").strip()
    if task:
        task_list.append(task)
        print(f" Task added: {task}")
    else:
        print(" Task cannot be empty!")


def view_tasks(task_list):
    if not task_list:
        print(" No tasks available.")
    else:
        print(" Current Tasks:")
        for idx, task in enumerate(task_list, start=1):
            print(f"{idx}. {task}")


def delete_task(task_list):
    if not task_list:
        print(" No task to delete.")
        return

    view_tasks(task_list)
    try:
        choice = int(input("Enter the task number to delete: "))
        if 1 <= choice <= len(task_list):
            removed = task_list.pop(choice - 1)
            print(f" Deleted task: '{removed}'")
        else:
            print(" Invalid task number.")
    except ValueError:
        print(" Please enter a valid number.")
    except Exception as e:
        print(f" An unexpected error occurred: {e}")


def main():
    tasks = []
    while True:
        try:
            display_menu()
            choice = input("Select an option (1-4): ").strip()

            if choice == '1':
                add_task(tasks)
            elif choice == '2':
                view_tasks(tasks)
            elif choice == '3':
                delete_task(tasks)
            elif choice == '4':
                print(" Goodbye!")
                break
            else:
                print(" Invalid choice. Please select a valid option.")
        except Exception as e:
            print(f" An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
