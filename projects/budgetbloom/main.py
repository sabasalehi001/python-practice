def get_valid_float_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value >= 0:
                return value
            else:
                print("Please enter a non-negative number.")
        except ValueError:
            print("Invalid input. Please enter a number.")


def calculate_budget(income, expenses, savings_goal):
    remaining_budget = income - expenses
    if remaining_budget < 0:
        print("Warning: Your expenses exceed your income!")

    savings_progress = min(income, savings_goal) / savings_goal * 100
    
    return remaining_budget, savings_progress


if __name__ == "__main__":
    print("Welcome to BudgetBloom!")

    income = get_valid_float_input("Enter your monthly income: ")
    expenses = get_valid_float_input("Enter your total monthly expenses: ")
    savings_goal = get_valid_float_input("Enter your desired monthly savings goal: ")

    remaining_budget, savings_progress = calculate_budget(income, expenses, savings_goal)

    print("\n--- Budget Summary ---")
    print(f"Remaining Budget: ${remaining_budget:.2f}")
    print(f"Savings Goal Progress: {savings_progress:.2f}%\n")

    if remaining_budget > 0:
        print("You have a positive budget. Keep up the good work!")
    elif remaining_budget == 0:
        print("Your budget is balanced. Consider ways to increase savings.")
    else:
        print("Review your expenses to ensure you reach your savings goal.")
