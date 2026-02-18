import sys

def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_primes_in_range(start, end):
    """Find all prime numbers within a given range."""
    primes = []
    for num in range(start, end + 1):
        if is_prime(num):
            primes.append(num)
    return primes

def get_user_input(prompt):
    """Get validated integer input from the user."""
    while True:
        try:
            value = int(input(prompt))
            if value < 0:
                print("Please enter a non-negative integer.")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter an integer.")


def main():
    """Main function to run the prime number finder."""
    start = get_user_input("Start of range: ")
    end = get_user_input("End of range: ")

    if start > end:
        print("Error: Start of range cannot be greater than end of range.")
        sys.exit(1)

    primes = find_primes_in_range(start, end)
    print(f"Prime numbers between {start} and {end}: {primes}")

if __name__ == "__main__":
    main()
