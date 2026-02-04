def get_valid_currency(prompt, valid_currencies):
    while True:
        currency = input(prompt).upper()
        if currency in valid_currencies:
            return currency
        else:
            print("Invalid currency. Please choose from:", ", ".join(valid_currencies))


def convert_currency(amount, source_currency, target_currency, exchange_rates):
    try:
        exchange_rate = exchange_rates[source_currency][target_currency]
        converted_amount = amount * exchange_rate
        return converted_amount
    except KeyError:
        print("Conversion rate not available.")
        return None


if __name__ == "__main__":
    exchange_rates = {
        "USD": {
            "EUR": 0.93, 
            "GBP": 0.79,
            "USD": 1.0
        },
        "EUR": {
            "USD": 1.07,
            "GBP": 0.85,
            "EUR": 1.0
        },
        "GBP": {
            "USD": 1.26,
            "EUR": 1.17,
            "GBP": 1.0
        }
    }

    valid_currencies = list(exchange_rates.keys())

    print("Welcome to AureusArbiter!")

    source_currency = get_valid_currency("Enter source currency (USD, EUR, GBP): ", valid_currencies)
    target_currency = get_valid_currency("Enter target currency (USD, EUR, GBP): ", valid_currencies)

    while True:
        try:
            amount = float(input("Enter amount to convert: "))
            if amount >= 0:
                break
            else:
                print("Amount must be non-negative.")
        except ValueError:
            print("Invalid amount. Please enter a number.")

    converted_amount = convert_currency(amount, source_currency, target_currency, exchange_rates)

    if converted_amount is not None:
        print(f"{amount:.2f} {source_currency} is equal to {converted_amount:.2f} {target_currency}")
