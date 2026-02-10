# GridGazer

GridGazer is a simple command-line tool for creating Markdown tables from user-provided data.

## Usage

Run `python main.py` and follow the prompts to enter the number of columns, column headers, and data rows.

## Example

```
Number of columns: 2
Column 1 header: Name
Column 2 header: Age
Number of rows: 2
Row 1, Column 1: Alice
Row 1, Column 2: 30
Row 2, Column 1: Bob
Row 2, Column 2: 25
```

Output:

```
| Name  | Age |
|-------|-----|
| Alice | 30  |
| Bob   | 25  |
```
