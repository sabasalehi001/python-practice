def get_exchange_rate(source_currency, target_currency):
    """Returns the exchange rate between two currencies."""
    rates = {
        ('USD', 'EUR'): 0.93,
        ('USD', 'GBP'): 0.79,
        ('EUR', 'USD'): 1.07,
        ('EUR', 'GBP'): 0.85,
        ('GBP', 'USD'): 1.27,
        ('GBP', 'EUR'): 1.18,
        ('USD', 'USD'): 1.00,
        ('EUR', 'EUR'): 1.00,
        ('GBP', 'GBP'): 1.00
    }

    if (source_currency, target_currency) in rates:
        return rates[(source_currency, target_currency)]
    else:
        return None


def convert_currency(amount, source_currency, target_currency):
    """Converts an amount from one currency to another."""
    rate = get_exchange_rate(source_currency, target_currency)

    if rate is None:
        return None
    else:
        return amount * rate


if __name__ == "__main__":
    try:
        amount = float(input("Enter amount: "))
        if amount < 0:
            print("Amount must be non-negative.")
            exit()
    except ValueError:
        print("Invalid amount. Please enter a number.")
        exit()

    source_currency = input("Enter source currency (USD, EUR, GBP): ").upper()
    if source_currency not in ['USD', 'EUR', 'GBP']:
        print("Invalid source currency. Please enter USD, EUR, or GBP.")
        exit()

    target_currency = input("Enter target currency (USD, EUR, GBP): ").upper()
    if target_currency not in ['USD', 'EUR', 'GBP']:
        print("Invalid target currency. Please enter USD, EUR, or GBP.")
        exit()

    converted_amount = convert_currency(amount, source_currency, target_currency)

    if converted_amount is None:
        print("Conversion not supported.")
    else:
        print(f"{amount} {source_currency} is equal to {converted_amount:.2f} {target_currency}")
