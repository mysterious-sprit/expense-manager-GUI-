import json
import os

DATA_FILE = "data.json"

# Load all expenses from the file
def load_expenses():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return []

# Save a new expense to the file
def save_expense(expense):
    expenses = load_expenses()
    expenses.append(expense)
    with open(DATA_FILE, "w") as file:
        json.dump(expenses, file, indent=4)
#end of the utils it is mainly used for saving a data .
