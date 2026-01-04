def validate_float_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value >= 0:
                return value
            else:
                print("Please enter a non-negative number.")
        except ValueError:
            print("Invalid input. Please enter a number.")


def savings_estimator():
    income = validate_float_input("Enter your monthly income: ")
    expenses = validate_float_input("Enter your monthly expenses: ")

    savings = income - expenses

    if savings > 0:
        print(f"Your estimated monthly savings: ${savings:.2f}")
    elif savings == 0:
        print("You are breaking even.")
    else:
        print(f"You are spending ${abs(savings):.2f} more than you earn each month.")


def debt_payoff_calculator():
    principal = validate_float_input("Enter the principal amount of your debt: ")
    interest_rate = validate_float_input("Enter the annual interest rate (as a percentage, e.g., 5 for 5%): ") / 100
    monthly_payment = validate_float_input("Enter your monthly payment: ")

    if monthly_payment <= (principal * interest_rate / 12): 
        print("Your monthly payment is not enough to cover the interest. You will never pay off the debt.")
        return

    months = 0
    while principal > 0:
        interest = principal * (interest_rate / 12)
        principal -= (monthly_payment - interest)
        months += 1
        if months > 1200:  # Safeguard against infinite loops (100 years)
            print("Calculation stopped.  Debt payoff is likely to take an extremely long time, or is impossible.")
            return

    years = months // 12
    remaining_months = months % 12
    print(f"Estimated time to pay off the debt: {years} years and {remaining_months} months.")


if __name__ == "__main__":
    print("Welcome to BudgetBuddyCLI!")

    while True:
        print("\nChoose an option:")
        print("1. Savings Estimator")
        print("2. Debt Payoff Calculator")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ")

        if choice == '1':
            savings_estimator()
        elif choice == '2':
            debt_payoff_calculator()
        elif choice == '3':
            print("Exiting BudgetBuddyCLI. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 3.")
