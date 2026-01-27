import json

def parse_weather_data(data):
    """Parses weather data from a string.

    Args:
        data: A string containing weather data in the format 'location,date,temperature,condition'.

    Returns:
        A dictionary containing the parsed weather data, or None if the data is invalid.
    """
    try:
        location, date, temperature, condition = data.split(',')
        temperature = int(temperature)
        if temperature < -100 or temperature > 100:  # Simple temperature validation
            print("Error: Invalid temperature value.")
            return None
        return {
            'location': location,
            'date': date,
            'temperature': temperature,
            'condition': condition
        }
    except ValueError:
        print("Error: Invalid data format. Please use location,date,temperature,condition")
        return None


def display_weather_data(weather_data):
    """Displays weather data in a user-friendly format.

    Args:
        weather_data: A dictionary containing weather data.
    """
    print(f"Weather data for {weather_data['location']} on {weather_data['date']}:")
    print(f"  Temperature: {weather_data['temperature']} degrees")
    print(f"  Condition: {weather_data['condition']}")


if __name__ == "__main__":
    while True:
        data = input("Enter weather data (location,date,temperature,condition - or 'exit'): ")
        if data.lower() == 'exit':
            break

        weather_data = parse_weather_data(data)

        if weather_data:
            display_weather_data(weather_data)
