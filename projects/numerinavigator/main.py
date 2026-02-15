import csv
import sys

def calculate_average(data, column_index):
    """Calculates the average of a specified column in a CSV data list."""
    try:
        values = [float(row[column_index]) for row in data[1:]] # Skip header row
        return sum(values) / len(values)
    except (ValueError, IndexError):
        return None

def find_maximum(data, column_index):
    """Finds the maximum value in a specified column in a CSV data list."""
    try:
        values = [float(row[column_index]) for row in data[1:]]
        return max(values)
    except (ValueError, IndexError):
        return None

def main():
    """Main function to parse arguments and perform CSV analysis."""
    if len(sys.argv) != 7:
        print("Usage: python main.py --file <filename> --column <column_number> --operation <average|max>")
        return

    try:
        filename = sys.argv[2]
        column_number = int(sys.argv[4])
        operation = sys.argv[6].lower()
    except ValueError:
        print("Error: Invalid input. Column number must be an integer.")
        return

    if operation not in ('average', 'max'):
        print("Error: Invalid operation. Choose 'average' or 'max'.")
        return

    try:
        with open(filename, 'r') as csvfile:
            reader = csv.reader(csvfile)
            data = list(reader)
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return
    except Exception as e:
        print(f"Error reading file: {e}")
        return

    if column_number <= 0:
        print("Error: Column number must be a positive integer.")
        return

    column_index = column_number - 1  # Adjust for 0-based indexing

    if operation == 'average':
        result = calculate_average(data, column_index)
        if result is not None:
            print(f"Average of column {column_number}: {result}")
        else:
            print(f"Error: Could not calculate average for column {column_number}. Check data type.")
    elif operation == 'max':
        result = find_maximum(data, column_index)
        if result is not None:
            print(f"Maximum value in column {column_number}: {result}")
        else:
            print(f"Error: Could not find maximum for column {column_number}. Check data type.")

if __name__ == "__main__":
    main()
