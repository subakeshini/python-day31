import os

FILENAME = "expenses.txt"

def add_expense():
    """Adds a new expense to the file."""
    category = input("📂 Enter expense category: ").strip()
    try:
        amount = float(input("💸 Enter amount: ₹"))
        date = input("📅 Enter date (YYYY-MM-DD): ").strip()
        with open(FILENAME, "a") as file:
            file.write(f"{category},{amount},{date}\n")
        print("✅ Expense added successfully!")
    except ValueError:
        print("❌ Invalid amount. Please enter a numeric value.")

def view_expenses():
    """Displays all expenses from the file."""
    if not os.path.exists(FILENAME):
        print("\n📭 No expenses recorded yet.")
        return
    with open(FILENAME, "r") as file:
        lines = file.readlines()
    if not lines:
        print("\n📭 No expenses recorded yet.")
        return
    print("\n📋 Expense Records:")
    print(f"{'Category':<15}{'Amount':<10}{'Date'}")
    print("-" * 35)
    for line in lines:
        category, amount, date = line.strip().split(",")
        print(f"{category:<15}₹{amount:<9}{date}")

def total_expenditure():
    """Calculates and displays the total expenditure."""
    if not os.path.exists(FILENAME):
        print("\n📭 No expenses recorded yet.")
        return
    total = 0
    with open(FILENAME, "r") as file:
        for line in file:
            try:
                _, amount, _ = line.strip().split(",")
                total += float(amount)
            except ValueError:
                continue
    print(f"\n🧮 Total Expenditure: ₹{total:.2f}")

# Main program loop
def run_expense_tracker():
    while True:
        print("\n💰 Expense Tracker Menu")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Total Expenditure")
        print("4. Exit")
        choice = input("🔢 Enter your choice (1-4): ").strip()
        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            total_expenditure()
        elif choice == "4":
            print("👋 Goodbye! Your expenses are saved.")
            break
        else:
            print("⚠️ Invalid choice. Please try again.")

# Run the tracker
run_expense_tracker()
