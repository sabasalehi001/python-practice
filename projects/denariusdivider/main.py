def validate_currency(currency):
    """Validates that the currency code is a 3-letter string."""
    if not isinstance(currency, str) or len(currency) != 3 or not currency.isalpha():
        return False
    return True


def exchange_currency(amount, rate):
    """Exchanges the given amount using the given rate."""
    try:
        amount = float(amount)
        rate = float(rate)
        if amount < 0 or rate < 0:
            raise ValueError("Amount and rate must be non-negative.")
        return amount * rate
    except ValueError as e:
        print(f"Error: Invalid input - {e}")
        return None


if __name__ == "__main__":
    while True:
        base_currency = input("Base Currency: ").upper()
        if not validate_currency(base_currency):
            print("Invalid base currency. Please enter a 3-letter currency code.")
            continue

        target_currency = input("Target Currency: ").upper()
        if not validate_currency(target_currency):
            print("Invalid target currency. Please enter a 3-letter currency code.")
            continue

        try:
            exchange_rate = input(f"Exchange Rate ({base_currency} to {target_currency}): ")
            exchange_rate = float(exchange_rate)
            if exchange_rate <= 0:
                print("Exchange rate must be positive.")
                continue
        except ValueError:
            print("Invalid exchange rate. Please enter a number.")
            continue

        try:
            amount = input(f"Amount in {base_currency}: ")
            amount = float(amount)
            if amount < 0:
                print("Amount must be non-negative.")
                continue
        except ValueError:
            print("Invalid amount. Please enter a number.")
            continue

        converted_amount = exchange_currency(amount, exchange_rate)

        if converted_amount is not None:
            print(f"{amount:.2f} {base_currency} is equal to {converted_amount:.2f} {target_currency}")

        another_conversion = input("Perform another conversion? (yes/no): ").lower()
        if another_conversion != 'yes':
            break
