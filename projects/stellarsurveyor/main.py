import random

def generate_sector(x, y):
    """Generates a sector of the galaxy with a possible planet."""
    planet = None
    if random.random() < 0.3:
        planet = {
            'name': f'Planet {chr(65 + random.randint(0, 25))}{random.randint(10, 99)}',
            'resources': random.randint(10, 100)
        }
    return {
        'x': x,
        'y': y,
        'planet': planet
    }

def display_sector(sector):
    """Displays the sector in ASCII art."""
    print(""" 
    +-------+
    |       |
    |       |
    +-------+
    """)
    print(f"Sector: ({sector['x']}, {sector['y']})")
    if sector['planet']:
        print(f"Planet Detected: {sector['planet']['name']} (Resources: {sector['planet']['resources']})")
    else:
        print("No planets detected.")

def main():
    """Main game loop."""
    x, y = 0, 0
    fuel = 100
    galaxy = {}

    while True:
        if (x, y) not in galaxy:
            galaxy[(x, y)] = generate_sector(x, y)

        sector = galaxy[(x, y)]
        display_sector(sector)

        print(f"Fuel: {fuel}")
        direction = input("Enter direction (N/S/E/W/Q): ").upper()

        if direction == 'N':
            y += 1
        elif direction == 'S':
            y -= 1
        elif direction == 'E':
            x += 1
        elif direction == 'W':
            x -= 1
        elif direction == 'Q':
            print("Exiting StellarSurveyor. Goodbye!")
            break
        else:
            print("Invalid direction. Please use N, S, E, W, or Q.")
            continue

        fuel -= 5
        if fuel <= 0:
            print("Out of fuel! Game over.")
            break

if __name__ == "__main__":
    main()
