from expense import Expense
import calendar
import datetime
import sys
import os

def main():
    
    expense_file_path = 'expenses.csv'
    budget_file_path  = 'budget.txt'  # File to store the budget
    args = sys.argv
    
    if len(args) == 2 and args[1] == 'log':
        #user input
        expense = get_user_expense()
        print(expense)
        #write their responses into a file
        save_to_file(expense, expense_file_path)

    if len(args) == 2 and args[1] == 'start': #intended to be run when a new budget it set
        budget = start(budget_file_path)

    if len(args) == 2 and args[1] == 'summarize':

        #read file and summarize it
        budget = load_budget(budget_file_path)
        if budget is None:
            print("No budget set. Please run the program with 'start' to set a budget.")
        else:
            summarize_expenses(expense_file_path, budget)


def start(budget_file_path):
    # Get budget from the user
    budget = int(input("What is your budget: "))

    # Save the budget to the config file
    with open(budget_file_path, 'w') as f:
        f.write(str(budget))
    print(f"Budget of ${budget} recorded.")
    return budget


def load_budget(budget_file_path):
    # Check if the config file exists
    if not os.path.exists(budget_file_path):
        return None

    # Read the budget from the file
    with open(budget_file_path, 'r') as f:
        budget = int(f.read().strip())
    return budget


def get_user_expense():
    print(f"🎯 get user expenses")
    expense_name = input("Enter the Expense name: ")
    expense_amount = float(input("Enter the Expense Amount: "))
    expense_category = [
        "🍟 Food",
        "🔟 Tithe",
        "🚗 Transportation",
        "📚 Schooling",
        "💩 Unnessesary"
    ]

    while True:
        print("Select a Category: ")
        for i, category_name in enumerate(expense_category):
            print( f" {i + 1}. {category_name}")
        value_range = f"[1 - {len(expense_category)}]"
        selected_index = int(input(f" Select a category number {value_range} : ")) - 1

        if selected_index in range(len(expense_category)):
            selected_category = expense_category[selected_index]
            new_expense = Expense(name = expense_name, category = selected_category, amount = expense_amount)
            return new_expense
        else: 
            print(" Invalid Category, please try again")
        
def save_to_file(expense : Expense, expense_file_path):
    print(f"🎯 Expense Saved to {expense_file_path}")
    with open(expense_file_path, 'a') as f:
        f.write(f"{expense.name}, {expense.amount}, {expense.category} \n")

def summarize_expenses(expense_file_path, budget):
    print(f"🎯 summarize spending")
    expenses: list[Expense] = []
    with open(expense_file_path, 'r') as f:
        lines = f.readlines()
        for line in lines:
            expense_name, expense_amount, expense_category = line.strip().split(",") 
            line_expense = Expense(
                name = expense_name, 
                amount = float(expense_amount),
                category = expense_category
            )
            expenses.append(line_expense)

    amount_by_category = {}
    for expense in expenses:
        key = expense.category
        if key in amount_by_category:
            amount_by_category[key] += expense.amount
        else:
            amount_by_category[key] = expense.amount
    for key, amount in amount_by_category.items():
        print(f"  {key}: ${amount:.2f}")
    total_spent = sum([x.amount for x in expenses])
    print(f"💵 Total Spent: ${total_spent:.2f}")

    remaining_budget = budget - total_spent
    print(f"✅ Budget Remaining: ${remaining_budget:.2f}")

    now = datetime.datetime.now()
    days_in_month = calendar.monthrange(now.year, now.month)[1]
    remaining_days = days_in_month - now.day
    daily_budget = remaining_budget / remaining_days
    print(f"👉 Budget Per Day: ${daily_budget:.2f}")

    
if __name__ == "__main__":
    main()