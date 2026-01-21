def draw_square(char, size):
    """Draws a square pattern.

    Args:
        char: The character to use for drawing.
        size: The size of the square.
    """
    if size <= 0:
        print("Size must be a positive integer.")
        return

    for _ in range(size):
        print(char * size)


def draw_triangle(char, size):
    """Draws a right-angled triangle pattern.

    Args:
        char: The character to use for drawing.
        size: The size of the triangle.
    """
    if size <= 0:
        print("Size must be a positive integer.")
        return

    for i in range(1, size + 1):
        print(char * i)


def main():
    """Main function to run the pattern printing program."""
    while True:
        pattern_type = input("Pattern type (square or triangle): ").lower()
        if pattern_type not in ['square', 'triangle']:
            print("Invalid pattern type. Please choose 'square' or 'triangle'.")
            continue
        else:
            break

    while True:
        char = input("Character: ")
        if len(char) != 1:
            print("Please enter a single character.")
            continue
        else:
            break

    while True:
        try:
            size = int(input("Size: "))
            if size <= 0:
                print("Size must be a positive integer.")
                continue
            break
        except ValueError:
            print("Invalid size. Please enter an integer.")

    if pattern_type == 'square':
        draw_square(char, size)
    else:
        draw_triangle(char, size)


if __name__ == "__main__":
    main()
