# Discount Calculator for a Shopping Store

# Step 1: Get the total bill amount
bill = float(input("Enter your total bill amount (₹): "))

# Step 2: Determine the discount rate
if bill >= 5000:
    discount_rate = 0.20
elif bill >= 3000:
    discount_rate = 0.10
elif bill >= 1000:
    discount_rate = 0.05
else:
    discount_rate = 0.0

# Step 3: Calculate discount and final amount
discount = bill * discount_rate
final_amount = bill - discount

# Step 4: Display the results
print(f"\nDiscount Applied: ₹{discount:.2f}")
print(f"Final Bill Amount: ₹{final_amount:.2f}")
