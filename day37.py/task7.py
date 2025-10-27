# 🎓 Student Marks Analyzer using Tuples

# Step 1: Create a tuple with marks of 5 subjects
marks = (85, 92, 78, 90, 88)

# Step 2: Analyze the marks using tuple functions
total = sum(marks)
highest = max(marks)
lowest = min(marks)
average = total / len(marks)

# Display results
print("📊 Student Marks Analysis:")
print(f"Marks         : {marks}")
print(f"Total Marks   : {total}")
print(f"Highest Marks : {highest}")
print(f"Lowest Marks  : {lowest}")
print(f"Average Marks : {average:.2f}")

# Step 3: Convert tuple to list, modify a mark, convert back to tuple
marks_list = list(marks)
marks_list[2] = 95  # Updating the 3rd subject mark
updated_marks = tuple(marks_list)

# Display updated marks
print("\n🛠️ Updated Marks After Modification:")
print(f"Modified Tuple: {updated_marks}")
