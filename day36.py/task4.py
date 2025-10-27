# 🔐 Simple Password Generator

# Step 1: Take user input
first_name = input("Enter your first name: ").strip()
last_name = input("Enter your last name: ").strip()
keyword = input("Enter a secret keyword: ").strip()

# Step 2: String slicing and reversing
first_part = first_name[:3]           # First 3 letters of first name
last_part = last_name[-3:]            # Last 3 letters of last name
reversed_keyword = keyword[::-1]      # Reverse the keyword

# Step 3: Concatenate and mix case
raw_password = first_part + last_part + reversed_keyword
password = raw_password[:len(raw_password)//2].lower() + raw_password[len(raw_password)//2:].upper()

# Step 4: Display the formatted password
print("\n🔑 Generated Password:")
print(f"Your secure password is: {password}")
