def get_currency_rate(base_currency, target_currency):
    """Returns the exchange rate between two currencies."""
    rates = {
        "USD": {"EUR": 0.92, "GBP": 0.79, "USD": 1.00},
        "EUR": {"USD": 1.09, "GBP": 0.86, "EUR": 1.00},
        "GBP": {"USD": 1.27, "EUR": 1.16, "GBP": 1.00},
    }

    if base_currency in rates and target_currency in rates[base_currency]:
        return rates[base_currency][target_currency]
    else:
        return None


def convert_currency(base_currency, target_currency, amount):
    """Converts an amount from one currency to another."""
    rate = get_currency_rate(base_currency, target_currency)

    if rate is None:
        return None

    return amount * rate


def main():
    """Main function to handle user input and output."""
    print("Currency Conversion Calculator")

    while True:
        base_currency = input("Base Currency (USD, EUR, GBP): ").upper()
        if base_currency not in ["USD", "EUR", "GBP"]:
            print("Invalid base currency. Please choose from USD, EUR, or GBP.")
            continue
        break

    while True:
        target_currency = input("Target Currency (USD, EUR, GBP): ").upper()
        if target_currency not in ["USD", "EUR", "GBP"]:
            print("Invalid target currency. Please choose from USD, EUR, or GBP.")
            continue
        break

    while True:
        try:
            amount = float(input("Amount to convert: "))
            if amount < 0:
                print("Amount must be non-negative.")
                continue
            break
        except ValueError:
            print("Invalid amount. Please enter a number.")

    converted_amount = convert_currency(base_currency, target_currency, amount)

    if converted_amount is None:
        print("Conversion failed. Please check your currencies.")
    else:
        print(f"{amount:.2f} {base_currency} is equal to {converted_amount:.2f} {target_currency}")


if __name__ == "__main__":
    main()
