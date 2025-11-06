import json
from datetime import datetime

DATA_FILE = "finance_data.json"

def load_from_file():
    try:
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {"income": [], "expenses": []}

def save_to_file(data):
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)

def add_income(amount, description):
    data = load_from_file()
    transaction = {
        "amount": amount,
        "description": description,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    data["income"].append(transaction)
    save_to_file(data)

def add_expense(amount, description):
    data = load_from_file()
    transaction = {
        "amount": amount,
        "description": description,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    data["expenses"].append(transaction)
    save_to_file(data)

def get_balance():
    data = load_from_file()
    total_income = sum(item["amount"] for item in data["income"])
    total_expenses = sum(item["amount"] for item in data["expenses"])
    return total_income - total_expenses

def get_transaction_history():
    return load_from_file()
