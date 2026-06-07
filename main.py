from expenses import add_expense, view_expenses, total_expense
from habits import view_habits, add_habit, mark_habit_done
from scraper import crypto_prices


print(" WELCOME TO LIFE TRACKER!")
print("1. Add Expense")
print("2. View Expenses")
print("3. Total Expense")
print("4. Add Habit")
print("5. View Habit")
print("6. Mark Habit Done")
print("7. View Crypto Prices")
print("8. Exit")

while True:
    choice = input("Choose an option (1-8): ").strip()

    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        total_expense()
    elif choice == "4":
        add_habit()
    elif choice == "5":
        view_habits()
    elif choice == "6":
        mark_habit_done()   
    elif choice == "7":
        crypto_prices()
    elif choice == "8":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please choose a valid option (1-8).")