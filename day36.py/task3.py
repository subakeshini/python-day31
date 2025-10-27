# 🧑‍💻 User Profile Formatter

# Step 1: Take user input
full_name = input("Enter your full name: ").strip().title()
age = str(input("Enter your age: ").strip())
quote = input("Enter your favorite quote: ").strip().upper()

# Step 2: Format and display the profile
profile = f"""
User Profile: -------------------------
Name           : {full_name}
Age            : {age}
Favorite Quote : \"{quote}\"
-------------------------
"""

print(profile)
