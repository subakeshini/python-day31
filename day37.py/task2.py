# ✅ To-Do List Manager

# Initialize an empty to-do list
todo_list = []

# Function to add a task
def add_task(task):
    todo_list.append({'task': task, 'completed': False})
    print(f"🆕 Task '{task}' added!")

# Function to mark a task as completed
def mark_completed(task):
    for item in todo_list:
        if item['task'] == task:
            item['completed'] = True
            print(f"✅ Task '{task}' marked as completed!")
            return
    print("⚠️ Task not found!")

# Function to remove a task
def remove_task(task):
    for item in todo_list:
        if item['task'] == task:
            todo_list.remove(item)
            print(f"🗑️ Task '{task}' removed!")
            return
    print("⚠️ Task not found!")

# Function to display pending tasks
def display_tasks():
    pending = [item for item in todo_list if not item['completed']]
    if not pending:
        print("\n📭 No pending tasks!")
    else:
        print("\n📋 Pending Tasks:")
        for index, item in enumerate(pending, start=1):
            print(f"{index}. {item['task']}")

# Menu-driven program
while True:
    print("\n📌 Menu:")
    print("1. Add Task")
    print("2. Mark Task as Completed")
    print("3. Remove Task")
    print("4. View Pending Tasks")
    print("5. Exit")

    try:
        choice = int(input("Enter your choice (1-5): "))
    except ValueError:
        print("⚠️ Please enter a valid number.")
        continue

    if choice == 1:
        task = input("Enter task: ").strip()
        add_task(task)

    elif choice == 2:
        task = input("Enter task to mark as completed: ").strip()
        mark_completed(task)

    elif choice == 3:
        task = input("Enter task to remove: ").strip()
        remove_task(task)

    elif choice == 4:
        display_tasks()

    elif choice == 5:
        print("👋 Exiting To-Do List Manager. Goodbye!")
        break

    else:
        print("⚠️ Invalid choice! Please try again.")
