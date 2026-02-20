def get_risk_tolerance():
    while True:
        risk_tolerance = input("Enter your risk tolerance (low, medium, high): ").lower()
        if risk_tolerance in ['low', 'medium', 'high']:
            return risk_tolerance
        else:
            print("Invalid input. Please enter 'low', 'medium', or 'high'.")


def allocate_funds(investment_amount, risk_tolerance):
    try:
        investment_amount = float(investment_amount)
        if investment_amount <= 0:
            print("Investment amount must be a positive number.")
            return None
    except ValueError:
        print("Invalid investment amount. Please enter a number.")
        return None

    if risk_tolerance == 'low':
        stocks = 0.2
        bonds = 0.7
        real_estate = 0.1
    elif risk_tolerance == 'medium':
        stocks = 0.5
        bonds = 0.3
        real_estate = 0.2
    else:
        stocks = 0.8
        bonds = 0.1
        real_estate = 0.1

    stock_allocation = investment_amount * stocks
    bond_allocation = investment_amount * bonds
    real_estate_allocation = investment_amount * real_estate

    return {
        'stocks': stock_allocation,
        'bonds': bond_allocation,
        'real_estate': real_estate_allocation
    }


if __name__ == "__main__":
    print("Welcome to AetheriumAllocator!")

    risk_tolerance = get_risk_tolerance()
    investment_amount = input("Enter the amount of Aetherium you want to invest: ")

    allocation = allocate_funds(investment_amount, risk_tolerance)

    if allocation:
        print("\nSuggested Allocation:")
        print(f"Stocks: {allocation['stocks']:.2f} Aetherium")
        print(f"Bonds: {allocation['bonds']:.2f} Aetherium")
        print(f"Real Estate: {allocation['real_estate']:.2f} Aetherium")
