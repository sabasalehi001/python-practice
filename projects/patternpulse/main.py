def generate_square_pattern(size):
    """Generates a square pattern of the given size."""
    for i in range(size):
        print('*' * size)


def generate_triangle_pattern(size):
    """Generates a right-angled triangle pattern of the given size."""
    for i in range(1, size + 1):
        print('*' * i)


def generate_diamond_pattern(size):
    """Generates a diamond pattern of the given size."""
    for i in range(1, size + 1):
        print(' ' * (size - i) + '*' * (2 * i - 1))
    for i in range(size - 1, 0, -1):
        print(' ' * (size - i) + '*' * (2 * i - 1))


def get_pattern_choice():
    """Gets the pattern choice from the user."""
    while True:
        pattern_type = input("Enter pattern type (square, triangle, diamond): ").lower()
        if pattern_type in ['square', 'triangle', 'diamond']:
            return pattern_type
        else:
            print("Invalid pattern type. Please choose from square, triangle, or diamond.")


def get_pattern_size():
    """Gets the pattern size from the user."""
    while True:
        try:
            size = int(input("Enter pattern size (positive integer): "))
            if size > 0:
                return size
            else:
                print("Size must be a positive integer.")
        except ValueError:
            print("Invalid input. Please enter a number.")


if __name__ == "__main__":
    pattern_type = get_pattern_choice()
    size = get_pattern_size()

    if pattern_type == 'square':
        generate_square_pattern(size)
    elif pattern_type == 'triangle':
        generate_triangle_pattern(size)
    elif pattern_type == 'diamond':
        generate_diamond_pattern(size)
