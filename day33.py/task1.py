# Simple Calculator

# Step 1: Get user input
num1 = float(input("Enter the first number: "))
operator = input("Enter an operator (+, -, *, /, %): ")
num2 = float(input("Enter the second number: "))

# Step 2: Perform calculation based on operator
if operator == '+':
    result = num1 + num2
elif operator == '-':
    result = num1 - num2
elif operator == '*':
    result = num1 * num2
elif operator == '/':
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error: Division by zero"
elif operator == '%':
    if num2 != 0:
        result = num1 % num2
    else:
        result = "Error: Modulo by zero"
else:
    result = "Invalid operator"

# Step 3: Display result
print(f"\nResult: {result}")
