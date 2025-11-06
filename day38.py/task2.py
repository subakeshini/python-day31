# Inventory Management System

# 1. Create an empty dictionary to store product details
inventory = {}

# 2. Add a new product
def add_product(product_id, name, price, quantity):
    inventory[product_id] = {
        "name": name,
        "price": price,
        "quantity": quantity
    }
    print(f"✅ Product '{name}' added successfully!")

# 3. Update product information (price or quantity)
def update_product(product_id, key, value):
    if product_id in inventory:
        if key in inventory[product_id]:
            inventory[product_id][key] = value
            print(f"🔄 Product {product_id} updated successfully!")
        else:
            print(f"⚠️ Key '{key}' not found in product record.")
    else:
        print("❌ Product not found!")

# 4. Remove a product
def remove_product(product_id):
    if product_id in inventory:
        removed_name = inventory[product_id]["name"]
        del inventory[product_id]
        print(f"🗑️ Product '{removed_name}' (ID: {product_id}) removed successfully!")
    else:
        print("❌ Product not found!")

# 5. Display all products
def display_inventory():
    if inventory:
        print("\n📦 Current Inventory:")
        for product_id, details in inventory.items():
            print(f"ID: {product_id}, Name: {details['name']}, Price: ₹{details['price']}, Quantity: {details['quantity']}")
    else:
        print("📭 No products in inventory.")

# Example Usage
add_product(1, "Laptop", 800, 10)
add_product(2, "Mouse", 20, 50)
update_product(1, "price", 750)
remove_product(2)
display_inventory()
