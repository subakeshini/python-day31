# 1. greet_user()
def greet_user():
    print("Hello, User!")
print(" ", end=" "); greet_user()
# 2. calculate_sum(a, b)
def calculate_sum(a, b):
    return a + b
print(" Sum:", calculate_sum(5, 3))
# 3. check_positive(num)
def check_positive(num):
    if num > 0:
        return "Positive"
    else:
        pass  # No action for non-positive numbers
print("Check Positive:", check_positive(10))
# 4. find_max(a, b, c)
def find_max(a, b, c):
    return max(a, b, c)
print("Max:", find_max(10, 25, 7))
# 5. global and local variable demonstration
count = 10  # Global variable

def modify_global():
    global count
    count += 5
    print("Inside function, count =", count)
print("Global count before:", count); modify_global(); print("Global count after:", count)
# 6. modify_variable() with local scope
def modify_variable():
    message = "Local Scope"
    print("Inside function:", message)

# Outside the function
message = "Global Scope"
print("Outside function:", message); modify_variable()
# 7. Recursive factorial(n)
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)
print(" Factorial of 5:", factorial(5))
# 8. Recursive fibonacci(n)
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)
print(" Fibonacci of 6:", fibonacci(6))
# 9. sum_numbers(*args)
def sum_numbers(*args):
    return sum(args)
print("Sum of numbers:", sum_numbers(1, 2, 3, 4))
# 10. print_student_details(**kwargs)
def print_student_details(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
print("Student Details:"); print_student_details(name="Alice", age=20, grade="A")
# 11. apply_operation(func, a, b)
def apply_operation(func, a, b):
    return func(a, b)
print("Operation Result:", apply_operation(lambda x, y: x + y, 4, 6))
# 12. outer_function() with inner()
def outer_function():
    def inner():
        return "Hello from Inner Function"
    return inner()
print(" ", outer_function())
# 13. map() to double each element
numbers = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, numbers))
print(" Doubled List:", doubled)
# --- Sample Calls ---
