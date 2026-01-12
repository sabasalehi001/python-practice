def get_float_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("Please enter a positive number.")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter a number.")

def get_currency_input(prompt):
    while True:
        currency = input(prompt).upper()
        if len(currency) != 3 or not currency.isalpha():
            print("Invalid currency code. Please enter a 3-letter code (e.g., USD).")
        else:
            return currency

def convert_currency(amount, from_currency, to_currency):
    # Sample exchange rates (no external API calls)
    exchange_rates = {
        ('USD', 'EUR'): 0.85,
        ('EUR', 'USD'): 1.18,
        ('USD', 'JPY'): 110.0,
        ('JPY', 'USD'): 0.0091,
        ('EUR', 'JPY'): 130.0,
        ('JPY', 'EUR'): 0.0077
    }

    key = (from_currency, to_currency)
    if key in exchange_rates:
        rate = exchange_rates[key]
        converted_amount = amount * rate
        return converted_amount
    else:
        return None

if __name__ == "__main__":
    print("Welcome to AurumAlchemist!")

    amount = get_float_input("Enter the amount to convert: ")
    from_currency = get_currency_input("Enter the starting currency (e.g., USD): ")
    to_currency = get_currency_input("Enter the target currency (e.g., EUR): ")

    converted_amount = convert_currency(amount, from_currency, to_currency)

    if converted_amount is not None:
        print(f"{amount:.2f} {from_currency} is equal to {converted_amount:.2f} {to_currency}")
    else:
        print("Exchange rate not available for the specified currencies.")
