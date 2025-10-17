# Simple Personal Info Formatter

# Step 1: Collect user input
name = input("Enter your name: ")
age = input("Enter your age: ")
height = input("Enter your height (in cm): ")

# Step 2: Display formatted output
print("\n--- Personal Information ---")
print(f"Name   : {name}")
print(f"Age    : {age} years")
print(f"Height : {height} cm")
print("----------------------------")
print(f"Hello {name},you are {age} years old and {height} cm tall.")