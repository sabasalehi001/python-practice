import random

def is_valid_direction(direction):
    return direction.upper() in ['N', 'S', 'E', 'W']


def move(x, y, direction):
    distance = random.randint(1, 3)
    if direction.upper() == 'N':
        y += distance
    elif direction.upper() == 'S':
        y -= distance
    elif direction.upper() == 'E':
        x += distance
    elif direction.upper() == 'W':
        x -= distance
    return x, y, distance


def main():
    x = 0
    y = 0
    exit_x = random.randint(5, 10)
    exit_y = random.randint(5, 10)

    print("You are in a cave.")

    while True:
        direction = input("What direction do you want to go? (N/S/E/W): ")

        if not is_valid_direction(direction):
            print("Invalid direction. Please enter N, S, E, or W.")
            continue

        new_x, new_y, distance = move(x, y, direction)

        if new_x < 0 or new_x > 15 or new_y < 0 or new_y > 15:
            print("You hit a wall!")
        else:
            x = new_x
            y = new_y
            print(f"You moved {direction.upper()} {distance} units.")

        if abs(x - exit_x) < 2 and abs(y - exit_y) < 2:
            print("You found the exit!")
            print("You win!")
            break

if __name__ == "__main__":
    main()
