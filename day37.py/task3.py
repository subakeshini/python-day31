# 🎓 Student Grades Management using Tuples

# Tuple storing student names and grades
students = ("Alice", "Bob", "Charlie", "David")
grades = (85, 92, 78, 90)

# 1. View all student grades
print("📋 Student Grades:")
for i in range(len(students)):
    print(f"{students[i]}: {grades[i]}")

# 2. Get highest, lowest, and average grade
print("\n📊 Statistics:")
print(f"Highest Grade : {max(grades)}")
print(f"Lowest Grade  : {min(grades)}")
print(f"Average Grade : {sum(grades) / len(grades):.2f}")

# 3. Access a student's grade using their index
student_name = "Charlie"
if student_name in students:
    index = students.index(student_name)
    print(f"\n🔍 {student_name}'s Grade: {grades[index]}")
else:
    print(f"\n⚠️ Student '{student_name}' not found.")
