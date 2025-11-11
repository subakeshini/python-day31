# To-Do List using File Handling

def display_tasks():
    """Displays all tasks from the file."""
    try:
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()
        if not tasks:
            print("\n📭 No tasks available.")
        else:
            print("\n📝 Your Tasks:")
            for index, task in enumerate(tasks, start=1):
                print(f"{index}. {task.strip()}")
    except FileNotFoundError:
        print("\n📂 No tasks found. Start by adding new tasks!")

def add_task():
    """Adds a new task to the file."""
    task = input("➕ Enter a new task: ").strip()
    if task:
        with open("tasks.txt", "a") as file:
            file.write(task + "\n")
        print("✅ Task added successfully!")
    else:
        print("⚠️ Task cannot be empty.")

def remove_task():
    """Removes a task from the file."""
    try:
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()
        if not tasks:
            print("\n📭 No tasks to remove.")
            return
        display_tasks()
        task_num = int(input("\n❌ Enter the task number to remove: "))
        if 1 <= task_num <= len(tasks):
            removed = tasks.pop(task_num - 1).strip()
            with open("tasks.txt", "w") as file:
                file.writelines(tasks)
            print(f"✅ Task '{removed}' removed successfully!")
        else:
            print("⚠️ Invalid task number!")
    except ValueError:
        print("❌ Please enter a valid number.")
    except FileNotFoundError:
        print("📂 No tasks file found.")

# Main program loop
def run_todo_list():
    while True:
        print("\n📋 To-Do List Menu")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Exit")
        choice = input("🔢 Enter your choice (1-4): ").strip()
        if choice == "1":
            display_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            remove_task()
        elif choice == "4":
            print("👋 Goodbye! Your tasks are saved.")
            break
        else:
            print("⚠️ Invalid choice. Please try again.")

# Run the program
run_todo_list()
