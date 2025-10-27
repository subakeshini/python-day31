# 🎓 Student Grade Tracker

# Initialize an empty list to store student data
students = []

# Function to add a student
def add_student(name, grade):
    students.append([name, grade])
    print(f"✅ Student '{name}' with grade '{grade}' added!")

# Function to update a grade
def update_grade(name, new_grade):
    for student in students:
        if student[0] == name:
            student[1] = new_grade
            print(f"🔁 Grade for '{name}' updated to '{new_grade}'")
            return
    print("⚠️ Student not found!")

# Function to remove a student
def remove_student(name):
    global students
    students = [student for student in students if student[0] != name]
    print(f"🗑️ Student '{name}' removed!")

# Function to display all students
def display_students():
    if not students:
        print("\n📭 No students in the list.")
    else:
        print("\n📋 Student List:")
        for student in students:
            print(f"{student[0]}: {student[1]}")

# Menu-driven program
while True:
    print("\n📌 Menu:")
    print("1. Add Student")
    print("2. Update Grade")
    print("3. Remove Student")
    print("4. Display Students")
    print("5. Exit")

    try:
        choice = int(input("Enter your choice (1-5): "))
    except ValueError:
        print("⚠️ Please enter a valid number.")
        continue

    if choice == 1:
        name = input("Enter student name: ").strip().title()
        grade = input("Enter grade: ").strip().upper()
        add_student(name, grade)

    elif choice == 2:
        name = input("Enter student name to update: ").strip().title()
        new_grade = input("Enter new grade: ").strip().upper()
        update_grade(name, new_grade)

    elif choice == 3:
        name = input("Enter student name to remove: ").strip().title()
        remove_student(name)

    elif choice == 4:
        display_students()

    elif choice == 5:
        print("👋 Exiting Student Grade Tracker. Goodbye!")
        break

    else:
        print("⚠️ Invalid choice. Please select from 1 to 5.")
