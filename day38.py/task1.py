# Student Database System

# 1. Create an empty dictionary to store student details
students = {}

# 2. Add a new student
def add_student(student_id, name, age, course):
    students[student_id] = {
        "name": name,
        "age": age,
        "course": course
    }
    print(f"✅ Student {name} added successfully!")

# 3. Update student information
def update_student(student_id, key, value):
    if student_id in students:
        if key in students[student_id]:
            students[student_id][key] = value
            print(f"🔄 Student {student_id} updated successfully!")
        else:
            print(f"⚠️ Key '{key}' not found in student record.")
    else:
        print("❌ Student not found!")

# 4. Remove a student
def remove_student(student_id):
    if student_id in students:
        del students[student_id]
        print(f"🗑️ Student {student_id} removed successfully!")
    else:
        print("❌ Student not found!")

# 5. Display all students
def display_students():
    if students:
        print("\n📋 Student Database:")
        for student_id, details in students.items():
            print(f"ID: {student_id}, Name: {details['name']}, Age: {details['age']}, Course: {details['course']}")
    else:
        print("📭 No students in the database.")

# Example Usage
add_student(101, "Alice", 20, "Computer Science")
add_student(102, "Bob", 21, "Mathematics")
update_student(101, "age", 21)
remove_student(102)
display_students()
