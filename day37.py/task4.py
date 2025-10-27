# 🧾 Inventory Management System using Tuples

# 1. Inventory Tuple (Item Name, Price)
inventory = (
    ("Laptop", 70000),
    ("Mouse", 1500),
    ("Keyboard", 2500),
    ("Monitor", 12000)
)

# 2. Display all inventory items
print("📦 Inventory Items:")
for item in inventory:
    print(f"- {item[0]}: ₹{item[1]}")

# 3. Search for a specific item
search_item = "Mouse"
found = next((item for item in inventory if item[0].lower() == search_item.lower()), None)

if found:
    print(f"\n🔍 {search_item} is available at ₹{found[1]}")
else:
    print(f"\n❌ {search_item} is not available in the inventory.")

# 4. Remove an item from inventory
remove_item = "Keyboard"
inventory = tuple(item for item in inventory if item[0].lower() != remove_item.lower())

# Display updated inventory
print("\n🗂️ Updated Inventory (After Removing Keyboard):")
for item in inventory:
    print(f"- {item[0]}: ₹{item[1]}")
