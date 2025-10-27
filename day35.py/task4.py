from functools import reduce

# 1. Function to calculate average score
def calculate_average(*args):
    return sum(args) / len(args)

# 2. Lambda + map to convert marks to grades
def convert_to_grades(marks):
    return list(map(lambda m: 'A' if m >= 90 else 'B' if m >= 80 else 'C' if m >= 70 else 'F', marks))

# 3. Filter function to find passing students
def filter_passed_students(student_records):
    return list(filter(lambda s: s['grade'] != 'F', student_records))

# 4. Use reduce to find highest score
def find_highest_score(student_records):
    return reduce(lambda x, y: x if x['average'] > y['average'] else y, student_records)

# 5. Recursive function to print first n students
def print_students_recursively(student_records, n, index=0):
    if index < n and index < len(student_records):
        s = student_records[index]
        print(f"Student: {s['name']}, Age: {s['age']}, Average Score: {s['average']}, Grade: {s['grade']}")
        print_students_recursively(student_records, n, index + 1)

# 6. Store student details dynamically using **kwargs
def create_student(**kwargs):
    return kwargs

# --- Sample Data ---
students = [
    create_student(name="John", age=16, marks=[85, 90, 80]),
    create_student(name="Emily", age=17, marks=[95, 92, 98]),
    create_student(name="Sam", age=15, marks=[60, 65, 58]),
    create_student(name="Lily", age=16, marks=[72, 75, 78]),
    create_student(name="Tom", age=17, marks=[45, 50, 55])
]

# Process each student: calculate average and assign grade
student_records = []
for s in students:
    avg = calculate_average(*s['marks'])
    grade = convert_to_grades([avg])[0]
    student_records.append({
        'name': s['name'],
        'age': s['age'],
        'average': round(avg, 2),
        'grade': grade
    })

# Display first n students using recursion
print("\n📋 Student Details:")
print_students_recursively(student_records, n=5)

# Filter passed students
passed = filter_passed_students(student_records)
print("\n✅ Passed Students:", [s['name'] for s in passed])

# Find highest scorer
topper = find_highest_score(student_records)
print(f"\n🏆 Highest Score: {topper['average']} by {topper['name']}")
