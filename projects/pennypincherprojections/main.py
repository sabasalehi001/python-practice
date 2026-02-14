import json

def get_float_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value >= 0:
                return value
            else:
                print("Please enter a non-negative number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def calculate_savings(initial_deposit, monthly_deposit, annual_interest_rate, years):
    """Calculates the projected savings based on recurring deposits and interest."""
    monthly_interest_rate = annual_interest_rate / 12 / 100
    months = years * 12
    total_savings = initial_deposit

    for _ in range(months):
        total_savings += monthly_deposit
        total_savings *= (1 + monthly_interest_rate)

    return total_savings

if __name__ == "__main__":
    print("Welcome to PennyPincherProjections!")

    initial_deposit = get_float_input("Initial Deposit: ")
    monthly_deposit = get_float_input("Monthly Deposit: ")
    annual_interest_rate = get_float_input("Annual Interest Rate (%): ")
    years = int(get_float_input("Number of Years: "))

    projected_savings = calculate_savings(initial_deposit, monthly_deposit, annual_interest_rate, years)

    print(f"\nProjected Savings: ${projected_savings:.2f}")
