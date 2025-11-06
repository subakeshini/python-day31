class ATM:
    def __init__(self, balance=0):
        self.__balance = balance  # Private attribute

    # Check current balance
    def check_balance(self):
        print(f"🏦 Your balance is: ${self.__balance}")

    # Deposit money
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"💰 ${amount} deposited successfully!")
        else:
            print("⚠️ Deposit amount must be positive.")

    # Withdraw money
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"💵 ${amount} withdrawn successfully!")
        else:
            print("❌ Insufficient balance or invalid amount.")

# Create ATM object and test functionality
user1 = ATM(1000)
user1.check_balance()
user1.deposit(500)
user1.check_balance()
user1.withdraw(300)
user1.check_balance()
user1.withdraw(1500)  # Should display insufficient balance
