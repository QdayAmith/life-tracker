from expenses import add_expense, view_expenses, total_expense

print(" WELCOME TO LIFE TRACKER!")
print("1. Add Expense")
print("2. View Expenses")
print("3. Total Expense")
print("4. Exit")

while True:
    choice = input("Choose an option (1-4): ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        total_expense()
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please choose a valid option (1-4).")