import csv

FILENAME = "students.csv"

def add_student():
    """Adds a new student to the CSV file."""
    name = input("👤 Enter student name: ").strip()
    age = input("🎂 Enter student age: ").strip()
    grade = input("📊 Enter student grade: ").strip()
    if name and age and grade:
        with open(FILENAME, "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([name, age, grade])
        print("✅ Student record added successfully!")
    else:
        print("⚠️ All fields are required.")

def view_students():
    """Displays all students from the CSV file."""
    try:
        with open(FILENAME, "r") as file:
            reader = csv.reader(file)
            students = list(reader)
            if not students:
                print("\n📭 No student records found.")
                return
            print("\n📋 Student Records:")
            print(f"{'Name':<15}{'Age':<5}{'Grade'}")
            print("-" * 30)
            for student in students:
                print(f"{student[0]:<15}{student[1]:<5}{student[2]}")
    except FileNotFoundError:
        print("\n📂 No student records found.")

def search_student():
    """Searches for a student by name."""
    search_name = input("🔍 Enter student name to search: ").strip().lower()
    try:
        with open(FILENAME, "r") as file:
            reader = csv.reader(file)
            found = False
            for student in reader:
                if student[0].strip().lower() == search_name:
                    print(f"\n✅ Found: Name: {student[0]}, Age: {student[1]}, Grade: {student[2]}")
                    found = True
                    break
            if not found:
                print("❌ Student not found!")
    except FileNotFoundError:
        print("\n📂 No student records found.")

# Main program loop
def run_student_manager():
    while True:
        print("\n📚 Student Record Manager")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Exit")
        choice = input("🔢 Enter your choice (1-4): ").strip()
        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            print("👋 Goodbye! Student records saved.")
            break
        else:
            print("⚠️ Invalid choice. Please try again.")

# Run the program
run_student_manager()
