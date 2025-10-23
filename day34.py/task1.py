def calculate_average(students):
    total = 0
    count = 0
    for marks in students.values():
        if marks != -1:
            total += marks
            count += 1
    return total / count if count > 0 else 0

def display_rankings(students):
    print("Student Rankings:")
    for index, (name, marks) in enumerate(students.items(), start=1):
        if marks == -1:
            continue
        print(f"{index}. {name} - {marks} marks")

def display_top_performers(students, threshold=80):
    print("\nTop Performers:")
    for name, marks in students.items():
        if marks >= threshold:
            print(f"🏆 {name} - {marks} marks")

# Sample data
students = {
    "John": 85,
    "Emma": 92,
    "Liam": 78,
    "Olivia": -1,  # Absent
    "Sophia": 90,
    "James": 65
}

# Run analyzer
display_rankings(students)
average = calculate_average(students)
print(f"\nClass Average Marks: {average:.2f}")
display_top_performers(students)
