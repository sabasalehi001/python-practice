# TabularTapir

A simple command-line tool for generating Markdown tables from user input.

## Usage

Run `python main.py` and follow the prompts to enter the table headers and data.

## Example

```
$ python main.py

Enter the table headers, separated by commas (e.g., Name,Age,City):
Name,Age,City

Enter the first row of data, separated by commas (e.g., John,30,New York):
John,30,New York

Enter the next row of data, separated by commas (or type 'done' to finish):
Jane,25,London

Enter the next row of data, separated by commas (or type 'done' to finish):
done

| Name | Age | City |
|---|---|---|
| John | 30 | New York |
| Jane | 25 | London |
```
