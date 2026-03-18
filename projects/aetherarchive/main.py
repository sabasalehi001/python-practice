import csv
import sys

def get_column_data(filename, column_index):
    try:
        with open(filename, 'r') as csvfile:
            reader = csv.reader(csvfile)
            data = [row[column_index] for row in reader if len(row) > column_index]
            return data
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        sys.exit(1)
    except IndexError:
        print(f"Error: Column index {column_index} out of range.")
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)

def analyze_data(data):
    unique_values = set(data)
    value_counts = {}
    for value in data:
        value_counts[value] = value_counts.get(value, 0) + 1
    most_frequent = max(value_counts, key=value_counts.get)

    try:
        numeric_data = [float(x) for x in data]
        minimum = min(numeric_data)
        maximum = max(numeric_data)
        return unique_values, most_frequent, minimum, maximum
    except ValueError:
        return unique_values, most_frequent, None, None

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python main.py <csv_file> <column_index>")
        sys.exit(1)

    csv_file = sys.argv[1]
    try:
        column_index = int(sys.argv[2])
        if column_index < 0:
            raise ValueError
    except ValueError:
        print("Error: Column index must be a non-negative integer.")
        sys.exit(1)

    data = get_column_data(csv_file, column_index)
    if not data:
        print("No data found in the specified column.")
        sys.exit(1)

    unique_values, most_frequent, minimum, maximum = analyze_data(data)

    print(f"Number of unique values: {len(unique_values)}")
    print(f"Most frequent value: {most_frequent}")
    if minimum is not None and maximum is not None:
        print(f"Minimum value: {minimum}")
        print(f"Maximum value: {maximum}")
