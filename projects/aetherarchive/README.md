# AetherArchive

A simple command-line tool to analyze CSV data.

## Usage

```bash
python main.py <csv_file> <column_index>
```

Where:

*   `<csv_file>` is the path to the CSV file you want to analyze.
*   `<column_index>` is the integer index of the column you want to get stats for (starting from 0).

## Example

If you have a file named `data.csv` and want to analyze the second column (index 1):

```bash
python main.py data.csv 1
```

## Output

The program will output the following statistics for the specified column:

*   Number of unique values.
*   Most frequent value.
*   Minimum and Maximum (if the data are numbers).
