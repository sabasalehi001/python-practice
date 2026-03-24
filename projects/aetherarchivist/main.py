import sys

def parse_weather_data(data_string):
    """Parses a weather data string and returns a dictionary."""
    weather_data = {}
    try:
        for item in data_string.split(','):
            key, value = item.split('=')
            weather_data[key.strip()] = value.strip()
        return weather_data
    except ValueError:
        return None

def display_weather_data(weather_data):
    """Displays weather data in a user-friendly format."""
    if not weather_data:
        print("Error: Invalid weather data format.")
        return

    city = weather_data.get('City', 'Unknown')
    temp = weather_data.get('Temp', 'Unknown')
    humidity = weather_data.get('Humidity', 'Unknown')
    wind = weather_data.get('Wind', 'Unknown')

    print(f"Weather for: {city}")
    print(f"Temperature: {temp}")
    print(f"Humidity: {humidity}")
    print(f"Wind Speed: {wind}")


def validate_data(weather_data):
    if not weather_data:
        return False

    if 'Temp' in weather_data:
        temp = weather_data['Temp']
        if 'C' not in temp and 'F' not in temp:
            print("Error: Temperature must include units (C or F).")
            return False
    if 'Wind' in weather_data:
        wind = weather_data['Wind']
        if 'kmh' not in wind and 'mph' not in wind:
            print("Error: Wind speed must include units (kmh or mph).")
            return False
    return True



if __name__ == "__main__":
    default_data = "City=DefaultCity,Temp=20C,Humidity=70%,Wind=10kmh"
    if len(sys.argv) > 1:
        weather_string = sys.argv[1]
    else:
        weather_string = default_data

    weather_data = parse_weather_data(weather_string)

    if validate_data(weather_data):
        display_weather_data(weather_data)
