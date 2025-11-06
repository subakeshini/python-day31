import finance

def show_menu():
    print("\n📊 Personal Finance Tracker")
    print("1. Add Income")
    print("2. Add Expense")
    print("3. View Balance")
    print("4. View Transaction History")
    print("5. Exit")

while True:
    show_menu()
    choice = input("Choose an option: ")

    if choice == "1":
        amount = float(input("Enter income amount: ₹"))
        desc = input("Enter income description: ")
        finance.add_income(amount, desc)
        print("✅ Income recorded.")

    elif choice == "2":
        amount = float(input("Enter expense amount: ₹"))
        desc = input("Enter expense description: ")
        finance.add_expense(amount, desc)
        print("✅ Expense recorded.")

    elif choice == "3":
        balance = finance.get_balance()
        print(f"\n💰 Current Balance: ₹{balance:.2f}")

    elif choice == "4":
        data = finance.get_transaction_history()
        print("\n📥 Income:")
        for item in data["income"]:
            print(f"  ₹{item['amount']} - {item['description']} ({item['timestamp']})")
        print("\n📤 Expenses:")
        for item in data["expenses"]:
            print(f"  ₹{item['amount']} - {item['description']} ({item['timestamp']})")

    elif choice == "5":
        print("👋 Exiting. Stay financially wise!")
        break

    else:
        print("❌ Invalid option. Try again.")
