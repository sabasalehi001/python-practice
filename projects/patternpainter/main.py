def generate_checkerboard(size):
    ""Generates a checkerboard pattern of the given size.""    
    if size <= 0:
        return "Size must be a positive integer."
    pattern = ""
    for i in range(size):
        for j in range(size):
            if (i + j) % 2 == 0:
                pattern += "#"  
            else:
                pattern += " "  
        pattern += "\n"
    return pattern

def generate_triangle(size):
    ""Generates a right-angled triangle pattern of the given size.""    
    if size <= 0:
        return "Size must be a positive integer."
    pattern = ""
    for i in range(1, size + 1):
        pattern += "*" * i + "\n"
    return pattern

def generate_diamond(size):
    ""Generates a diamond pattern of the given size.""    
    if size <= 0:
        return "Size must be a positive integer."
    pattern = ""
    for i in range(1, size + 1):
        pattern += " " * (size - i) + "*" * (2 * i - 1) + "\n"
    for i in range(size - 1, 0, -1):
        pattern += " " * (size - i) + "*" * (2 * i - 1) + "\n"
    return pattern

def main():
    ""Main function to handle user input and pattern generation.""    
    print("Welcome to PatternPainter!")
    print("Available patterns:")
    print("1. Checkerboard")
    print("2. Triangle")
    print("3. Diamond")

    while True:
        try:
            choice = int(input("Enter the pattern number (1-3): "))
            if 1 <= choice <= 3:
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 3.")
        except ValueError:
            print("Invalid input. Please enter an integer.")

    while True:
        try:
            size = int(input("Enter the size of the pattern: "))
            if size > 0:
                break
            else:
                print("Size must be a positive integer.")
        except ValueError:
            print("Invalid input. Please enter an integer.")

    if choice == 1:
        pattern = generate_checkerboard(size)
    elif choice == 2:
        pattern = generate_triangle(size)
    elif choice == 3:
        pattern = generate_diamond(size)

    print(pattern)

if __name__ == "__main__":
    main()
