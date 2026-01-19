import json

WEATHER_DATA = {
    "Sunnyville": {
        "temperature": 25, 
        "humidity": 60, 
        "conditions": "Sunny"
    },
    "Rainyburg": {
        "temperature": 18, 
        "humidity": 90, 
        "conditions": "Rainy"
    },
    "Cloudyton": {
        "temperature": 22, 
        "humidity": 75, 
        "conditions": "Cloudy"
    }
}

def display_weather(location):
    """Displays the weather data for a given location."""
    if location in WEATHER_DATA:
        data = WEATHER_DATA[location]
        print(f"Weather in {location}:")
        print(f"  Temperature: {data['temperature']}°C")
        print(f"  Humidity: {data['humidity']}%")
        print(f"  Conditions: {data['conditions']}")
    else:
        print(f"Error: Location '{location}' not found.")

def get_valid_location():
    """Prompts the user for a location and validates the input."""
    while True:
        location = input("Enter a location (Sunnyville, Rainyburg, Cloudyton): ").strip()
        if location in WEATHER_DATA:
            return location
        else:
            print("Invalid location. Please choose from the list.")


if __name__ == "__main__":
    print("Welcome to AquaClarity!")
    location = get_valid_location()
    display_weather(location)
    print("\nThank you for using AquaClarity!")
