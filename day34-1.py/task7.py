# Triangle Pattern Generator

# Step 1: Get number of rows from the user
rows = int(input("Enter the number of rows: "))

# Step 2: Print triangle pattern
print("\nTriangle Pattern:")
for i in range(1, rows + 1, 2):  # Only odd rows for triangle shape
    print("* " * i)
