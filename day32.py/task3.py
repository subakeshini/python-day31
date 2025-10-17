print("subakeshini")
print("Welcome to Python Programming!\nLet's learn and grow together.")
name = "suba"
age = 25
favorite_color = "Blue"

print("Name:", name)
print("Age:", age)
print("Favorite Color:", favorite_color)

a = "Hello"       # string
b = 42            # integer
c = 3.14          # float
d = True          # boolean

print(type(a))
print(type(b))
print(type(c))
print(type(d))

name = input("Enter your name: ")
print(f"Welcome, {name}!")

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
sum = num1 + num2
print(f"The sum is: {sum}")

num = input("Enter a number: ")
print("Type before conversion:", type(num))
num = float(num)
print("Type after conversion:", type(num))

name = input("Enter your name: ")
age = input("Enter your age: ")
city = input("Enter your city: ")

print(f"{name} is {age} years old and lives in {city}.")

length = float(input("Enter the length: "))
width = float(input("Enter the width: "))
area = length * width

print(f"The area of the rectangle is {area} square units.")

item = input("Enter item name: ")
quantity = int(input("Enter quantity: "))
price = float(input("Enter price per item: "))
total = quantity * price

print(f"\n--- Receipt ---\nItem: {item}\nQuantity: {quantity}\nPrice: ₹{price:.2f}\nTotal: ₹{total:.2f}")

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

a, b = b, a

print(f"After swapping: a = {a}, b = {b}")

celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32

print(f"{celsius}°C is equal to {fahrenheit:.2f}°F")

name = input("Enter your name: ")
age = input("Enter your age: ")
height = input("Enter your height (in cm): ")
hobby = input("Enter your favorite hobby: ")

print(f"\n--- Profile ---\nName: {name}\nAge: {age}\nHeight: {height} cm\nHobby: {hobby}")
