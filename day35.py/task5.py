# Global transaction counter
total_transactions = 0

class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        global total_transactions
        self.balance += amount
        total_transactions += 1
        print(f"Deposited: ₹{amount}")

    def withdraw(self, amount):
        global total_transactions
        # Inner function to check withdrawal feasibility
        def can_withdraw():
            return self.balance >= amount + transaction_fee(amount)

        transaction_fee = lambda amt: amt * 0.02  # 2% fee

        if can_withdraw():
            fee = transaction_fee(amount)
            self.balance -= (amount + fee)
            total_transactions += 1
            print(f"Withdrawn: ₹{amount}")
            print(f"Transaction Fee: ₹{fee}")
        else:
            print("❌ Insufficient balance for withdrawal including fee.")

    def get_balance(self):
        print(f"Balance: ₹{self.balance}")

# First-class function to apply interest
def apply_interest(account, interest_func):
    account.balance = interest_func(account.balance)
    print(f"Interest Applied. New Balance: ₹{account.balance}")

# --- Sample Execution ---
account = BankAccount("Alice", 1000)
print(f"\nAccount Holder: {account.name}")
account.deposit(500)
account.withdraw(200)
account.get_balance()

# Apply 5% interest using first-class function
apply_interest(account, lambda bal: bal * 1.05)

print(f"\nTotal Transactions: {total_transactions}")
