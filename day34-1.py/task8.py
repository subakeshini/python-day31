# Simple To-Do List Manager

tasks = []

while True:
    print("\n1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("Type 'exit' to quit")

    choice = input("Enter your choice: ")

    if choice == '1':
        task = input("Enter a task: ")
        tasks.append(task)
        print("Task added.")

    elif choice == '2':
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

    elif choice == '3':
        num = int(input("Enter task number to remove: "))
        if 1 <= num <= len(tasks):
            tasks.pop(num - 1)
            print("Task removed.")
        else:
            print("Invalid number.")

    elif choice == 'exit':
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")
