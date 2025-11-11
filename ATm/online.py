# Custom Exception for Out of Stock
class OutOfStockError(Exception):
    """Raised when requested quantity exceeds available stock."""
    pass

# Sample product catalog with stock and price
store = {
    "Laptop": {"price": 50000, "stock": 5},
    "Phone": {"price": 20000, "stock": 10},
    "Headphones": {"price": 1500, "stock": 15},
    "Charger": {"price": 800, "stock": 20}
}

cart = {}

def display_store():
    print("\n🛍️ Available Products:")
    print(f"{'Product':<15}{'Price':<10}{'Stock'}")
    print("-" * 35)
    for item, details in store.items():
        print(f"{item:<15}₹{details['price']:<9}{details['stock']}")

def add_to_cart():
    display_store()
    try:
        product = input("Enter product name to add: ").strip()
        if product not in store:
            raise KeyError("Product not found in store.")
        quantity = int(input("Enter quantity: "))
        if quantity <= 0:
            raise ValueError("Quantity must be positive.")
        if quantity > store[product]["stock"]:
            raise OutOfStockError("Insufficient stock available.")
        cart[product] = cart.get(product, 0) + quantity
        store[product]["stock"] -= quantity
        print(f"✅ Added {quantity} x {product} to cart.")
    except KeyError as e:
        print("❌ Error:", e)
    except ValueError as e:
        print("❌ Error:", e)
    except OutOfStockError as e:
        print("❌ Error:", e)

def remove_from_cart():
    if not cart:
        print("🛒 Cart is empty.")
        return
    print("\n🗑️ Cart Items:")
    for item, qty in cart.items():
        print(f"{item}: {qty}")
    try:
        product = input("Enter product name to remove: ").strip()
        if product not in cart:
            raise KeyError("Product not found in cart.")
        quantity = int(input("Enter quantity to remove: "))
        if quantity <= 0 or quantity > cart[product]:
            raise ValueError("Invalid quantity.")
        cart[product] -= quantity
        store[product]["stock"] += quantity
        if cart[product] == 0:
            del cart[product]
        print(f"✅ Removed {quantity} x {product} from cart.")
    except KeyError as e:
        print("❌ Error:", e)
    except ValueError as e:
        print("❌ Error:", e)

def checkout():
    if not cart:
        print("🛒 Cart is empty. Add items before checkout.")
        return
    total = sum(store[item]["price"] * qty for item, qty in cart.items())
    print("\n🧾 Checkout Summary:")
    for item, qty in cart.items():
        print(f"{item}: {qty} x ₹{store[item]['price']} = ₹{qty * store[item]['price']}")
    print(f"Total Amount: ₹{total}")
    try:
        payment = float(input("Enter payment amount: ₹"))
        if payment < total:
            raise ValueError("Insufficient payment.")
        print(f"✅ Payment successful! Change returned: ₹{payment - total:.2f}")
        cart.clear()
    except ValueError as e:
        print("❌ Error:", e)

# Main program loop
def run_shopping_cart():
    while True:
        print("\n🛒 Shopping Cart Menu")
        print("1. View Store")
        print("2. Add to Cart")
        print("3. Remove from Cart")
        print("4. Checkout")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ").strip()
        if choice == "1":
            display_store()
        elif choice == "2":
            add_to_cart()
        elif choice == "3":
            remove_from_cart()
        elif choice == "4":
            checkout()
        elif choice == "5":
            print("👋 Thank you for shopping with us!")
            break
        else:
            print("⚠️ Invalid choice. Please try again.")

# Run the system
run_shopping_cart()
