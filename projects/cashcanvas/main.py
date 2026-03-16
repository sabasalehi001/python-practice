def get_valid_float_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value < 0:
                print("Please enter a non-negative value.")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter a number.")


def calculate_budget(income, expenses):
    total_expenses = sum(expenses.values())
    remaining_budget = income - total_expenses
    return remaining_budget


def main():
    print("Welcome to CashCanvas!")

    income = get_valid_float_input("Enter your monthly income: ")

    expenses = {}
    while True:
        expense_name = input("Enter an expense (or type 'done'): ")
        if expense_name.lower() == 'done':
            break
        
        expense_amount = get_valid_float_input(f"Enter the amount for {expense_name}: ")
        expenses[expense_name] = expense_amount

    remaining_budget = calculate_budget(income, expenses)

    print(f"\nYour remaining budget: ${remaining_budget:.2f}")


if __name__ == "__main__":
    main()
