import json

try:
    with open("data/expenses.json", "r") as file:
        collection_entries = json.load(file)
except FileNotFoundError:
    collection_entries = []

def add_expense():
    user_entries = {
        "amount" : float(input("Enter the amount to track your expenses:")),
        "category" : input("Enter the category of your expense:"),
        "description" : input("Enter the description of your expense :"),
        "date" : input("Enter the date of your expense (YYYY-MM-DD):")
    }
    collection_entries.append(user_entries)

    with open("data/expenses.json", "w") as file:
        json.dump(collection_entries, file)

    print("EXPENSE ADDED SUCCESSFULLY!")

add_expense()


def view_expenses():
    try:
        with open("data/expenses.json", "r") as file:
            collection_entries = json.load(file)
    except FileNotFoundError:
        collection_entries = []

    for entry in collection_entries:
        print("-" * 30)
        print(f"Amount: {entry['amount']}")
        print(f"Category: {entry['category']}")
        print(f"Description: {entry['description']}")
        print(f"Date: {entry['date']}")

    print("-" * 30)

view_expenses()


def total_expense():
    try:
        with(open("data/expenses.json", "r") as file):
            collection_entries = json.load(file)
    except FileNotFoundError:
        collection_entries = []

    total = sum(entry["amount"] for entry in collection_entries)
    print(f"Total Expense: {total}")    

total_expense()

print("-" * 30)
print("-" * 30)
        