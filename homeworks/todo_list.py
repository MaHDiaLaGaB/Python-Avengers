
tasks = []

while True:
    print("\nWhat would you like to do?")
    print("1) Add task")
    print("2) View tasks")
    print("3) Delete task")
    print("4) Exit")
    choice = input("> ").strip()

    if choice == "1":
        # Add a new task
        task = input("Enter task description: ").strip()
        if task:
            tasks.append(task)
            print(f'Task added: "{task}"')
        else:
            print("You didn't enter anything. No task added.")

    elif choice == "2":
        if not tasks:
            print("No tasks to show.")
        else:
            print("Task list:")
            idx = 1
            for t in tasks:
                print(f"{idx}. {t}")
                idx += 1

    elif choice == "3":
        if not tasks:
            print("No tasks to delete.")
        else:
            print("Enter the number of the task to delete:")
            idx = 1
            for t in tasks:
                print(f"{idx}. {t}")
                idx += 1

            to_delete = input("> ").strip()
            if to_delete.isdigit():
                index = int(to_delete)
                if 1 <= index <= len(tasks):
                    removed = tasks.pop(index - 1)
                    print(f'Task deleted: "{removed}"')
                else:
                    print("Invalid task number.")
            else:
                print("Please enter a valid number.")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Unknown choice, please try again.")

