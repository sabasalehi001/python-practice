def validate_input(prompt, data_type):
    while True:
        try:
            value = data_type(input(prompt))
            if value < 0:
                print("Please enter a non-negative value.")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter a number.")


def calculate_budget_balance(income, expenses):
    return income - expenses


if __name__ == "__main__":
    print("Welcome to BudgetBalanceBeacon!")

    monthly_income = validate_input("Enter your monthly income: ", float)
    current_expenses = validate_input("Enter your current monthly expenses: ", float)
    new_expense = validate_input("Enter the amount of the new expense: ", float)

    current_balance = calculate_budget_balance(monthly_income, current_expenses)
    new_expenses = current_expenses + new_expense
    new_balance = calculate_budget_balance(monthly_income, new_expenses)

    print(f"\nYour current budget balance is: ${current_balance:.2f}")
    print(f"Your budget balance after the new expense is: ${new_balance:.2f}")

    if new_balance < 0:
        print("Warning: Your budget is now in deficit!")
    elif new_balance == 0:
        print("Your budget is now balanced.")
    else:
        print("Your budget is still in surplus.")

    print("\nThank you for using BudgetBalanceBeacon!")
