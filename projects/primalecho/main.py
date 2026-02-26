import sys

def is_prime(n):
    """Checks if a number is prime."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def calculate_resonance(prime, start, end):
    """Calculates the resonance score of a prime within a range."""
    midpoint = (start + end) / 2
    return abs(prime - midpoint)


def main():
    """Main function to find and display prime numbers and their resonance."""
    if len(sys.argv) != 3:
        print("Usage: python main.py <start_number> <end_number>")
        return

    try:
        start = int(sys.argv[1])
        end = int(sys.argv[2])
    except ValueError:
        print("Error: Start and end numbers must be integers.")
        return

    if start >= end:
        print("Error: Start number must be less than end number.")
        return

    print("Prime Numbers and Resonance Scores:")
    for num in range(start, end + 1):
        if is_prime(num):
            resonance = calculate_resonance(num, start, end)
            print(f"{num}: Resonance = {resonance:.2f}")

if __name__ == "__main__":
    main()
