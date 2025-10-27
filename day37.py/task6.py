# 🛒 Shopping Cart System

# Initialize an empty cart
cart = []

# Function to add a product
def add_product(name, price):
    cart.append([name, price])
    print("Product added successfully!")

# Function to remove a product by name
def remove_product(name):
    for item in cart:
        if item[0].lower() == name.lower():
            cart.remove(item)
            print(f"Product '{name}' removed successfully!")
            return
    print("Product not found in cart!")

# Function to view cart and total price
def view_cart():
    if not cart:
        print("\n🛒 Shopping Cart is empty.")
    else:
        print("\n🛍️ Shopping Cart:")
        for item in cart:
            print(f"- {item[0]}: ₹{item[1]}")
        total_price = sum(item[1] for item in cart)
        print(f"\nTotal Items: {len(cart)}")
        print(f"Total Price: ₹{total_price}")

# Menu-driven loop
while True:
    print("\n1. Add Product")
    print("2. Remove Product")
    print("3. View Cart")
    print("4. Checkout")

    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("⚠️ Please enter a valid number.")
        continue

    if choice == 1:
        name = input("Enter Product Name: ").strip().title()
        try:
            price = int(input("Enter Price: "))
            add_product(name, price)
        except ValueError:
            print("⚠️ Please enter a valid price.")

    elif choice == 2:
        name = input("Enter Product Name to Remove: ").strip().title()
        remove_product(name)

    elif choice == 3:
        view_cart()

    elif choice == 4:
        print("\n🧾 Final Cart Summary:")
        view_cart()
        print("🛍️ Thank you for shopping with us!")
        break

    else:
        print("⚠️ Invalid choice! Please try again.")
