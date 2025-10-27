# Recursive To-Do List Manager

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, task):
        self.tasks = list(filter(lambda t: t != task, self.tasks))

    def show_tasks(self):
        if not self.tasks:
            print("No tasks available.")
        else:
            print("\nYour Tasks:")
            for t in self.tasks:
                print(f"- {t}")

    def manage_list(self):
        def menu():
            print("\n1. Add Task\n2. Remove Task\n3. Show Tasks\n4. Exit")
            return input("Choose an option: ")

        def process_choice(choice):
            if choice == '1':
                task = input("Enter task: ")
                self.add_task(task)
            elif choice == '2':
                task = input("Enter task to remove: ")
                self.remove_task(task)
            elif choice == '3':
                self.show_tasks()
            elif choice == '4':
                print("Exiting To-Do List...")
                return
            else:
                print("Invalid choice, try again!")

            self.manage_list()  # Recursive call

        process_choice(menu())  # Start recursion

# Run To-Do List Manager
todo = ToDoList()
todo.manage_list()
