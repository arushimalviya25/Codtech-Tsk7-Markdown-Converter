import json
import os
from datetime import datetime

DATA_FILE = "expenses.json"

def load_expenses():
    if not os.path.exists(DATA_FILE):
        return []
    try:
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    except json.JSONDecodeError:
        return []

def save_expenses(expenses):
    with open(DATA_FILE, "w") as file:
        json.dump(expenses, file, indent=4)

def add_expense(expenses):
    print("\n--- Add New Expense ---")
    try:
        amount = float(input("Enter amount spent: "))
    except ValueError:
        print("❌ Invalid amount. Please enter a valid number.")
        return
        
    category = input("Enter category (e.g., Food, Transport, Rent, Bills): ").strip()
    description = input("Enter brief description: ").strip()
    date_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    new_expense = {
        "amount": amount,
        "category": category if category else "Uncategorized",
        "description": description if description else "No description",
        "date": date_str
    }
    
    expenses.append(new_expense)
    save_expenses(expenses)
    print(f"🎉 Success! Added ${amount:.2f} under '{category}'.")

def view_expenses(expenses):
    print("\n--- Expense History ---")
    if not expenses:
        print("Your expense ledger is currently empty.")
        return
        
    print(f"{'Index':<6} | {'Date':<20} | {'Category':<15} | {'Amount':<10} | {'Description'}")
    print("-" * 75)
    for index, exp in enumerate(expenses, 1):
        print(f"{index:<6} | {exp['date']:<20} | {exp['category']:<15} | ${exp['amount']:<10.2f} | {exp['description']}")

def show_summary(expenses):
    print("\n--- Analytics Summary ---")
    if not expenses:
        print("No data available to calculate analytics.")
        return
        
    total_spent = sum(exp["amount"] for exp in expenses)
    print(f"Total Money Spent: ${total_spent:.2f}")
    
    category_totals = {}
    for exp in expenses:
        cat = exp["category"]
        category_totals[cat] = category_totals.get(cat, 0) + exp["amount"]
        
    print("\nBreakdown By Category:")
    for cat, total in category_totals.items():
        percentage = (total / total_spent) * 100
        print(f" * {cat:<15}: ${total:<8.2f} ({percentage:.1f}%)")

def main():
    expenses = load_expenses()
    
    while True:
        print("\n=============================")
        print("     PERSONAL EXPENSE TRACKER     ")
        print("=============================")
        print("1. Add New Expense")
        print("2. View Expense Ledger")
        print("3. View Analytics Summary")
        print("4. Exit Application")
        
        choice = input("\nSelect an option (1-4): ").strip()
        
        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
            show_summary(expenses)
        elif choice == "4":
            print("\nExiting tracker. Your data is safely saved locally. Goodbye!")
            break
        else:
            print("❌ Invalid input. Please choose a menu option between 1 and 4.")

if __name__ == "__main__":
    main()