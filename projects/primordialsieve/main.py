def is_prime(number):
    """Checks if a number is prime."""
    if number <= 1:
        return False
    if number <= 3:
        return True
    if number % 2 == 0 or number % 3 == 0:
        return False
    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6
    return True


def find_primes_in_range(start, end):
    """Finds all prime numbers within the given range."""
    primes = []
    for number in range(start, end + 1):
        if is_prime(number):
            primes.append(number)
    return primes


def main():
    """Main function to handle user input and output."""
    try:
        start = int(input("Enter the starting number of the range: "))
        end = int(input("Enter the ending number of the range: "))

        if start < 0 or end < 0:
            print("Error: Range limits must be non-negative.")
            return
        if start > end:
            print("Error: Starting number must be less than or equal to the ending number.")
            return

        primes = find_primes_in_range(start, end)

        if primes:
            print("Prime numbers in the range [{}, {}]:".format(start, end))
            print(primes)
        else:
            print("No prime numbers found in the range [{}, {}].".format(start, end))

    except ValueError:
        print("Error: Invalid input. Please enter integers only.")

if __name__ == "__main__":
    main()
