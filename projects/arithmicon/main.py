import json

def solve_missing_number(sequence):
    try:
        sequence = [int(x) for x in sequence.split(',')]
        if len(sequence) < 3:
            return "Sequence must have at least 3 numbers."
        
        diffs = [sequence[i+1] - sequence[i] for i in range(len(sequence)-1)]
        if len(set(diffs)) > 2: #Allow for slight error
             return "Could not reliably determine the missing number. Not a simple arithmetic sequence."
        
        if len(set(diffs)) == 1:
           step = diffs[0]
        else:
          step = sum(diffs) / len(diffs)
          
        for i in range(len(sequence) - 1):
            if sequence[i+1] - sequence[i] != step:
                return str(int(sequence[i] + step))
        return "No missing number found or sequence is complete"
    except ValueError:
        return "Invalid input. Please enter a comma-separated list of numbers."

def solve_target_sum(numbers, target):
    try:
        numbers = [int(x) for x in numbers.split(',')]
        target = int(target)
        for i in range(len(numbers)):
            for j in range(i + 1, len(numbers)):
                if numbers[i] + numbers[j] == target:
                    return f"{numbers[i]}, {numbers[j]}"
        return "No two numbers sum to the target."
    except ValueError:
        return "Invalid input. Please enter a comma-separated list of numbers and a target number."

def main():
    print("Welcome to Arithmicon!")

    while True:
        print("\nChoose a puzzle:")
        print("1. Missing Number")
        print("2. Target Sum")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ")

        if choice == '1':
            sequence = input("Enter the number sequence (comma-separated): ")
            result = solve_missing_number(sequence)
            print("Result:", result)
        elif choice == '2':
            numbers = input("Enter the list of numbers (comma-separated): ")
            target = input("Enter the target sum: ")
            result = solve_target_sum(numbers, target)
            print("Result:", result)
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 3.")

if __name__ == "__main__":
    main()
