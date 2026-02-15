# NumeriNavigator

A simple command-line tool for analyzing CSV data.

## Features

*   Calculates the average of a specified column in a CSV file.
*   Finds the maximum value in a specified column.

## Usage

```bash
python main.py --file data.csv --column 2 --operation average
python main.py --file data.csv --column 3 --operation max
```

## Example CSV (data.csv)

```csv
Name,Age,Score
Alice,30,85
Bob,25,92
Charlie,40,78
David,35,95
```

## Notes

*   The column argument is 1-indexed.
*   The CSV file should have a header row.
*   Error handling is included for invalid column numbers and file issues.
