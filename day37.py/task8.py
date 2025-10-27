# 🛒 Shopping Cart System using Tuples

# Initial cart with product names
cart = ("Laptop", "Mouse", "Keyboard", "Mouse", "Monitor")

# Function to view all products
def view_cart():
    print("\n📋 Current Shopping Cart:")
    for index, item in enumerate(cart, start=1):
        print(f"{index}. {item}")

# Function to add a product
def add_product(product):
    global cart
    cart_list = list(cart)
    cart_list.append(product)
    cart = tuple(cart_list)
    print(f"✅ '{product}' added to cart!")

# Function to remove a product
def remove_product(product):
    global cart
    cart_list = list(cart)
    if product in cart_list:
        cart_list.remove(product)
        cart = tuple(cart_list)
        print(f"🗑️ '{product}' removed from cart!")
    else:
        print("⚠️ Product not found in cart!")

# Function to count product occurrences
def count_product(product):
    count = cart.count(product)
    print(f"\n🔍 '{product}' appears {count} time(s) in the cart.")

# Function to display first three items
def show_first_three():
    print("\n📦 First Three Items in Cart:")
    print(cart[:3])

# Menu-driven loop
while True:
    print("\n📌 Menu:")
    print("1. View Cart")
    print("2. Add Product")
    print("3. Remove Product")
    print("4. Count Product Occurrence")
    print("5. Show First Three Items")
    print("6. Exit")

    try:
        choice = int(input("Enter your choice (1–6): "))
    except ValueError:
        print("⚠️ Please enter a valid number.")
        continue

    if choice == 1:
        view_cart()
    elif choice == 2:
        product = input("Enter product name to add: ").strip().title()
        add_product(product)
    elif choice == 3:
        product = input("Enter product name to remove: ").strip().title()
        remove_product(product)
    elif choice == 4:
        product = input("Enter product name to count: ").strip().title()
        count_product(product)
    elif choice == 5:
        show_first_three()
    elif choice == 6:
        print("👋 Exiting Shopping Cart System. Goodbye!")
        break
    else:
        print("⚠️ Invalid choice! Please try again.")
