# Simple Bill Calculator

# Step 1: Get user input
item_name = input("Enter the item name: ")
price = float(input("Enter the price of the item: ₹"))
quantity = int(input("Enter the quantity: "))
tax_rate = 0.18  # 18% GST

# Step 2: Calculate totals
subtotal = price * quantity
tax = subtotal * tax_rate
total = subtotal + tax

print(f"Type of item_name : {type(item_name)}") #'str'
print(f"Type of price:{type(price)}")#'float'
print(f"Type of quantity:{type(quantity)}")#int
print(f"Type of total:{type(total)}")#'float'
# Step 3: Display formatted bill
print("\n--- Bill Summary ---")
print(f"Item       : {item_name}")
print(f"Unit Price : ₹{price:.2f}")
print(f"Quantity   : {quantity}")
print(f"Subtotal   : ₹{subtotal:.2f}")
print(f"Tax (18%)  : ₹{tax:.2f}")
print(f"Total Bill : ₹{total:.2f}")
print("---------------------")
