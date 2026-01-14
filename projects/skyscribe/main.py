import json

def parse_weather_data(data):
    """Parses weather data string into a list of dictionaries."""
    weather_entries = []
    for entry in data.splitlines():
        if not entry:
            continue
        try:
            city, temp, condition = entry.split(',')
            city_name = city.split(':')[1]
            temperature = int(temp.split(':')[1])
            condition_desc = condition.split(':')[1]
            weather_entries.append({
                'city': city_name,
                'temperature': temperature,
                'condition': condition_desc
            })
        except (ValueError, IndexError):
            print("Invalid data format. Please use: City:Name,Temperature:Value,Condition:Description")
            return None
    return weather_entries


def display_weather_data(weather_data):
    """Displays weather data in a formatted manner."""
    if not weather_data:
        return
    print("\n--- Weather Report ---")
    for data in weather_data:
        print(f"City: {data['city']}")
        print(f"Temperature: {data['temperature']}°C")
        print(f"Condition: {data['condition']}\n")


if __name__ == "__main__":
    while True:
        weather_data_string = input("Enter weather data (one city per line, format: City:Name,Temperature:Value,Condition:Description, or type 'exit'):\n")
        if weather_data_string.lower() == 'exit':
            break

        weather_data = parse_weather_data(weather_data_string)
        if weather_data:
            display_weather_data(weather_data)

        another_input = input("Parse more data? (y/n): ").lower()
        if another_input != 'y':
            break

    print("SkyScribe signing off!")
