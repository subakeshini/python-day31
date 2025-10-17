# Simple Student Report Card

# Step 1: Collect student details
name = input("Enter student's name: ")
student_class = input("Enter class/grade: ")

# Step 2: Collect marks for three subjects
subject1 = float(input("Enter marks for Subject 1: "))
subject2 = float(input("Enter marks for Subject 2: "))
subject3 = float(input("Enter marks for Subject 3: "))

# Step 3: Calculate total and percentage
total_marks = subject1 + subject2 + subject3
percentage = (total_marks / 300) * 100  # Assuming each subject is out of 100

# Step 4: Display formatted report card
print("\n📄 --- Student Report Card ---")
print(f"Name       : {name}")
print(f"Class      : {student_class}")
print(f"Subject 1  : {subject1}")
print(f"Subject 2  : {subject2}")
print(f"Subject 3  : {subject3}")
print(f"Total      : {total_marks} / 300")
print(f"Percentage : {percentage:.2f}%")
print("------------------------------")
