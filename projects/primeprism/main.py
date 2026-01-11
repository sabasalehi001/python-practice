import json

def is_prime(number):
    """Checks if a number is prime."""
    if number <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True


def find_primes(start, end):
    """Finds prime numbers within a given range."""
    primes = []
    for number in range(start, end + 1):
        if is_prime(number):
            primes.append(number)
    return primes


if __name__ == "__main__":
    try:
        start = int(input("Enter the starting number: "))
        end = int(input("Enter the ending number: "))

        if start >= end:
            print("Error: Starting number must be less than the ending number.")
        elif start < 0 or end < 0:
            print("Error: Numbers must be non-negative.")
        else:
            prime_numbers = find_primes(start, end)
            print("\nPrime numbers between", start, "and", end, ":")
            for prime in prime_numbers:
                print(prime)
    except ValueError:
        print("Error: Invalid input. Please enter integers only.")
