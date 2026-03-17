def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True


def find_primes_in_range(start, end):
    primes = []
    for num in range(start, end + 1):
        if is_prime(num):
            primes.append(num)
    return primes


if __name__ == "__main__":
    while True:
        try:
            start = int(input("Enter the starting number of the range: "))
            end = int(input("Enter the ending number of the range: "))

            if start >= end:
                print("Invalid input: Start must be less than end.")
                continue
            if start < 0 or end < 0:
                print("Invalid input: Numbers must be non-negative.")
                continue

            break # Exit the loop if input is valid

        except ValueError:
            print("Invalid input: Please enter integers only.")

    prime_numbers = find_primes_in_range(start, end)

    if prime_numbers:
        print("Prime numbers in the range [{}, {}]: {}".format(start, end, prime_numbers))
    else:
        print("No prime numbers found in the range [{}, {}]".format(start, end))
