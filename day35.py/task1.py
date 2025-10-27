from functools import reduce

class Student:
    students_list = []  # Global list to store all student objects

    def __init__(self, name, age, *scores):
        self.name = name
        self.age = age
        self.scores = scores
        Student.students_list.append(self)

    def get_average(self):
        return sum(self.scores) / len(self.scores)

    @staticmethod
    def filter_passing_students():
        return list(filter(lambda s: s.get_average() >= 50, Student.students_list))

    @staticmethod
    def get_highest_score():
        return reduce(lambda x, y: x if x.get_average() > y.get_average() else y, Student.students_list)

    @staticmethod
    def display_students():
        print("\n📋 All Student Details:")
        for student in Student.students_list:
            print(f"Name: {student.name}, Age: {student.age}, Avg Score: {student.get_average():.2f}")

# Adding Student Records
s1 = Student("Alice", 20, 45, 78, 90)
s2 = Student("Bob", 21, 88, 92, 85)
s3 = Student("Charlie", 22, 40, 35, 30)

# Display All Students
Student.display_students()

# Filter and Display Passing Students
passing_students = Student.filter_passing_students()
print("\n✅ Passing Students:")
for student in passing_students:
    print(student.name)

# Find and Display Top Student
top_student = Student.get_highest_score()
print(f"\n🏆 Top Student: {top_student.name} with Avg Score: {top_student.get_average():.2f}")
