tasks = []

while True:
    print("\n1. Add Task\n2. View Tasks\n3. Remove Task\n4. Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        task = input("Enter task: ")
        tasks.append(task)
        print("Task added.")

    elif choice == 2:
        if tasks:
            print("Tasks:")
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")
        else:
            print("No tasks found.")

    elif choice == 3:
        if tasks:
            print("Tasks:")
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")
            index = int(input("Enter task number to remove: "))
            if 1 <= index <= len(tasks):
                removed = tasks.pop(index - 1)
                print(f"Removed task: {removed}")
            else:
                print("Invalid task number.")
        else:
            print("No tasks to remove.")

    elif choice == 4:
        print("Exiting program.")
        break

    else:
        print("Invalid choice. Try again.")
