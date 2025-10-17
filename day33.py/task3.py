a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print(f"Sum        : {a + b}")
print(f"Difference : {a - b}")
print(f"Product    : {a * b}")
print(f"Quotient   : {a / b if b != 0 else 'Undefined (division by zero)'}")
print(f"Remainder  : {a % b if b != 0 else 'Undefined (modulo by zero)'}")

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

if x > y:
    print("First number is greater than second.")
elif x < y:
    print("First number is less than second.")
else:
    print("Both numbers are equal.")
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

a = a + b
b = a - b
a = a - b

print(f"After swapping: a = {a}, b = {b}")

year = int(input("Enter a year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a Leap Year.")
else:
    print(f"{year} is not a Leap Year.")

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

largest = a
if b > largest:
    largest = b
if c > largest:
    largest = c

print(f"The largest number is: {largest}")

radius = float(input("Enter the radius: "))
area = 3.14 * radius ** 2
print(f"Area of the circle is: {area:.2f}")

num = float(input("Enter a number: "))

if num > 0:
    print("The number is Positive.")
elif num < 0:
    print("The number is Negative.")
else:
    print("The number is Zero.")

age = int(input("Enter your age: "))

if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")

# Grade Assignment Program

# Step 1: Get marks from the user
marks = float(input("Enter your marks: "))

# Step 2: Determine the grade
if marks >= 90:
    grade = "A"
elif marks >= 80:
    grade = "B"
elif marks >= 70:
    grade = "C"
elif marks >= 60:
    grade = "D"
else:
    grade = "Fail"

# Step 3: Display the result
print(f"Your grade is: {grade}")

# Simple ATM Withdrawal Program

# Step 1: Set initial balance
balance = 5000

# Step 2: Ask user for withdrawal amount
withdraw_amount = float(input("Enter amount to withdraw: ₹"))

# Step 3: Check if withdrawal is possible
if withdraw_amount > balance:
    print("Insufficient funds.")
else:
    balance -= withdraw_amount
    print(f"Withdrawal successful! Remaining balance: ₹{balance:.2f}")

# Divisibility Check Program

# Step 1: Get user input
number = int(input("Enter a number: "))

# Step 2: Check divisibility
if number % 5 == 0 and number % 11 == 0:
    print(f"{number} is divisible by both 5 and 11.")
else:
    print(f"{number} is NOT divisible by both 5 and 11.")

# Vowel or Consonant Checker

# Step 1: Get a single character from the user
char = input("Enter a single alphabet character: ").lower()

# Step 2: Check if it's a vowel or consonant
if len(char) == 1 and char.isalpha():
    if char in 'aeiou':
        print(f"{char} is a vowel.")
    else:
        print(f"{char} is a consonant.")
else:
    print("Invalid input. Please enter a single alphabet character.")

num = int(input("Enter a number: "))
print("Even" if num % 2 == 0 else "Odd")
