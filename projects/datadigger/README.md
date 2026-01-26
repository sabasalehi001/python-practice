# DataDigger

DataDigger is a simple command-line tool for analyzing CSV data.
It allows you to calculate basic statistics for a specified column in a CSV file.

## Usage

`python main.py <filepath> <column_index>`

Where:
*   `<filepath>` is the path to the CSV file.
*   `<column_index>` is the index of the column to analyze (0-based).

## Example

`python main.py data.csv 2`

This will calculate the sum and average of the values in the third column (index 2) of the `data.csv` file.

## Error Handling

The program handles invalid file paths, invalid column indices, and non-numeric data in the specified column.
