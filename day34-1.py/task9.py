# Simple Banking System

balance = 10000  # Starting balance

while True:
    print("\n1. Deposit")
    print("2. Withdraw")
    print("Type 'quit' to exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        amount = float(input("Enter deposit amount: "))
        balance += amount
        print(f"Deposited ₹{amount}")
        print(f"Current Balance: ₹{balance}")

    elif choice == '2':
        amount = float(input("Enter withdrawal amount: "))
        if amount <= balance:
            balance -= amount
            print(f"Withdrawn ₹{amount}")
        else:
            print("Insufficient funds.")
        print(f"Current Balance: ₹{balance}")

    elif choice == 'quit':
        print("Exiting Banking System. Goodbye!")
        break

    else:
        print("Invalid choice. Try again.")
