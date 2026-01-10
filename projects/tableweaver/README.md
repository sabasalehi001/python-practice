# TableWeaver

TableWeaver is a simple command-line tool for creating Markdown tables from user input. It prompts you for the column headers and then asks for each row of data.

## Usage

Run the script using `python main.py`. Follow the prompts to enter your table data. The script will then output the Markdown table.

## Example

```
python main.py
```

Follow the prompts to create a table:

Column headers (comma-separated): Name, Age, City
Row 1: Alice, 30, New York
Row 2: Bob, 25, London

Output:

```markdown
| Name  | Age | City      |
|-------|-----|-----------|
| Alice | 30  | New York  |
| Bob   | 25  | London    |
```
