# Custom Exception for invalid marks
class InvalidMarksError(Exception):
    """Custom exception for invalid marks."""
    pass

# Function to calculate grade based on marks
def calculate_grade(marks):
    """Determine grade based on marks."""
    if marks < 0 or marks > 100:
        raise InvalidMarksError("Marks should be between 0 and 100.")
    if marks >= 90:
        return "A"
    elif marks >= 75:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 40:
        return "D"
    else:
        return "F"

# Main program to take input and display grade
def run_grading_system():
    try:
        marks = float(input("🎯 Enter student marks (0-100): "))
        grade = calculate_grade(marks)
        print(f"✅ Student Grade: {grade}")
    except ValueError:
        print("❌ Error: Please enter a valid numeric value.")
    except InvalidMarksError as e:
        print("❌ Error:", e)

# Run the grading system
run_grading_system()
