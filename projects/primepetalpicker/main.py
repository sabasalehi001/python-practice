def is_prime(number):
    """Checks if a number is prime."""
    if number <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True


def find_primes_in_range(start, end):
    """Finds all prime numbers within a given range."""
    primes = []
    for number in range(start, end + 1):
        if is_prime(number):
            primes.append(number)
    return primes


if __name__ == "__main__":
    while True:
        try:
            start_num = int(input("Start number: "))
            end_num = int(input("End number: "))

            if start_num <= 0 or end_num <= 0:
                print("Please enter positive integers only.")
                continue

            if start_num > end_num:
                print("Start number must be less than or equal to the end number.")
                continue

            break # Exit loop after valid input

        except ValueError:
            print("Invalid input. Please enter integers only.")


    prime_numbers = find_primes_in_range(start_num, end_num)
    print(f"Prime numbers between {start_num} and {end_num}: {prime_numbers}")
