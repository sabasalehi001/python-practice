import sys

def draw_triangle(height, char):
    for i in range(1, height + 1):
        print(char * i)

def draw_square(side, char):
    for i in range(side):
        print(char * side)

def draw_diamond(size, char):
    for i in range(size):
        print(' ' * (size - i - 1) + char * (2 * i + 1))
    for i in range(size - 2, -1, -1):
        print(' ' * (size - i - 1) + char * (2 * i + 1))


def get_positive_integer(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
            else:
                print("Please enter a positive integer.")
        except ValueError:
            print("Invalid input. Please enter an integer.")

def get_character(prompt):
    while True:
        char = input(prompt)
        if len(char) == 1:
            return char
        else:
            print("Please enter a single character.")


if __name__ == "__main__":
    print("Welcome to ShapeShifterSketcher!")

    while True:
        print("\nChoose a pattern to draw:")
        print("1. Triangle")
        print("2. Square")
        print("3. Diamond")
        print("4. Quit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            height = get_positive_integer("Enter the height of the triangle: ")
            char = get_character("Enter the character to use: ")
            draw_triangle(height, char)
        elif choice == '2':
            side = get_positive_integer("Enter the side length of the square: ")
            char = get_character("Enter the character to use: ")
            draw_square(side, char)
        elif choice == '3':
            size = get_positive_integer("Enter the size of the diamond (half the width): ")
            char = get_character("Enter the character to use: ")
            draw_diamond(size, char)
        elif choice == '4':
            print("Goodbye!")
            sys.exit()
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")
