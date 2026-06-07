import json
from datetime import date, timedelta, datetime


try:
    with open("data/habits.json", "r") as file:
        habit_tracker = json.load(file)
except FileNotFoundError:
    habit_tracker = []


def add_habit():
    name = input("What is the name of your habit? ").strip()
    for entry in habit_tracker:
        if entry["name"] == name:
            print("Habit already exists. Please choose a different name.")
            return
    stats = {
        "name" :  name,
        "streak": 0,
        "last_updated": None
    }
    habit_tracker.append(stats)

    with open("data/habits.json", "w") as file:
        json.dump(habit_tracker, file)

    print("HABIT ADDED SUCCESSFULLY!")

# add_habit()



today = str(date.today())
yesterday = str(date.today() - timedelta(days=1))  

def mark_habit_done():
    name = input("Enter the name of the habit you completed: ").strip()
    for entry in habit_tracker:
        if entry["name"] == name:
            last_updated = entry["last_updated"]
            if last_updated is None or last_updated == yesterday:
                entry["streak"] += 1
                entry["last_updated"] = today
                print(f"Great job! Your streak for {name} is now {entry['streak']} days.")
            elif last_updated == today:
                print(f"You have already marked {name} as done today.")
            else:
                entry["streak"] = 1
                entry["last_updated"] = today
                print(f"Streak reset. Your streak for {name} is now 1 day.")
            with open("data/habits.json", "w") as file:
                json.dump(habit_tracker, file)
            break
    else:
        print("Habit not found. Please add the habit first.")

# mark_habit_done()


def view_habits():
    with open("data/habits.json", "r") as file:
        habit_tracker = json.load(file)
    for entry in habit_tracker:
        print("-" * 30)
        print(f"Habit: {entry['name']}")
        print(f"Current Streak: {entry['streak']} days")
        print(f"Last Updated: {entry['last_updated']}")

    print("-" * 30)

# view_habits()
