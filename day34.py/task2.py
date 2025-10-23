def generate_number_pyramid(rows):
    if rows < 0:
        print("Invalid input. Exiting...")
        return

    print("\nGenerated Number Pyramid:")
    for i in range(1, rows + 1):
        if i % 2 == 0:
            continue  # Skip even rows
        print((str(i) + " ") * i)

# Main Program
try:
    user_input = int(input("Enter number of rows for the pyramid: "))
    generate_number_pyramid(user_input)
except ValueError:
    print("Please enter a valid integer.")
