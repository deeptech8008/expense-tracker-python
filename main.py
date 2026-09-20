import json

# Load data
def load_data():
    try:
        with open("expenses.json", "r") as f:
            return json.load(f)
    except:
        return []

# Save data
def save_data(data):
    with open("expenses.json", "w") as f:
        json.dump(data, f, indent=4)

# Add expense
def add_expense(data):
    name = input("Enter expense name: ")
    amount = float(input("Enter amount: "))
    
    data.append({"name": name, "amount": amount})
    print("Expense added!")

# View expenses
def view_expenses(data):
    total = 0
    for exp in data:
        print(exp["name"], "-", exp["amount"])
        total += exp["amount"]
    
    print("Total:", total)

# Main
data = load_data()

while True:
    print("\n1. Add Expense")
    print("2. View Expenses")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_expense(data)
        save_data(data)

    elif choice == "2":
        view_expenses(data)

    elif choice == "3":
        break

    else:
        print("Invalid choice")