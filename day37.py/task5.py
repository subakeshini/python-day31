# 🎓 Student Management System using Lists

# Initialize an empty list to store student names
students = []

# Function to add a student
def add_student(name):
    students.append(name)
    print("Student added successfully!")

# Function to remove a student
def remove_student(name):
    if name in students:
        students.remove(name)
        print("Student removed successfully!")
    else:
        print("Student not found!")

# Function to update a student's name
def update_student(old_name, new_name):
    if old_name in students:
        index = students.index(old_name)
        students[index] = new_name
        print("Student name updated successfully!")
    else:
        print("Student not found!")

# Function to display all students
def show_students():
    print("Student List:", students)

# Menu-driven loop
while True:
    print("\n1. Add Student")
    print("2. Remove Student")
    print("3. Update Student Name")
    print("4. Show All Students")
    print("5. Exit")

    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Please enter a valid number.")
        continue

    if choice == 1:
        name = input("Enter Student Name: ").strip().title()
        add_student(name)

    elif choice == 2:
        name = input("Enter Student Name to Remove: ").strip().title()
        remove_student(name)

    elif choice == 3:
        old_name = input("Enter Current Student Name: ").strip().title()
        new_name = input("Enter New Student Name: ").strip().title()
        update_student(old_name, new_name)

    elif choice == 4:
        show_students()

    elif choice == 5:
        print("Exiting Student Management System. Goodbye!")
        break

    else:
        print("Invalid choice! Please try again.")
