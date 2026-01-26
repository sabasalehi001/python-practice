import csv
import sys

def calculate_stats(data):
    """Calculates the sum and average of a list of numbers."""
    total = sum(data)
    average = total / len(data)
    return total, average


def process_csv(filepath, column_index):
    """Reads a CSV file and extracts data from the specified column."""
    try:
        with open(filepath, 'r') as csvfile:
            reader = csv.reader(csvfile)
            data = []
            for row in reader:
                try:
                    value = float(row[column_index])
                    data.append(value)
                except (IndexError, ValueError):
                    print(f"Warning: Skipping invalid data in row: {row}")
                    continue
            if not data:
                print("Error: No valid numeric data found in the specified column.")
                return None, None

            return calculate_stats(data)
    except FileNotFoundError:
        print(f"Error: File not found at path: {filepath}")
        return None, None
    except IndexError:
        print("Error: Column index out of range.")
        return None, None


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python main.py <filepath> <column_index>")
        sys.exit(1)

    filepath = sys.argv[1]
    try:
        column_index = int(sys.argv[2])
        if column_index < 0:
            raise ValueError
    except ValueError:
        print("Error: Column index must be a non-negative integer.")
        sys.exit(1)

    total, average = process_csv(filepath, column_index)

    if total is not None and average is not None:
        print(f"Sum: {total}")
        print(f"Average: {average}")
