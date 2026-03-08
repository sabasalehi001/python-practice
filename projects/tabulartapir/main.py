import sys

def validate_input(headers, data):
    """Validates that the number of columns in each row matches the number of headers."""
    num_headers = len(headers)
    for row in data:
        if len(row) != num_headers:
            return False
    return True


def create_markdown_table(headers, data):
    """Generates a Markdown table from the given headers and data."""
    header_row = "| " + " | ".join(headers) + " |"
    separator_row = "|" + "---" * len(headers) + "|"
    data_rows = ["| " + " | ".join(row) + " |" for row in data]

    table = "\n".join([header_row, separator_row] + data_rows)
    return table


if __name__ == "__main__":
    print("Enter the table headers, separated by commas (e.g., Name,Age,City):")
    headers_input = input()
    headers = [h.strip() for h in headers_input.split(",")]

    data = []
    while True:
        print("Enter the next row of data, separated by commas (or type 'done' to finish):")
        data_input = input()
        if data_input.lower() == "done":
            break
        row = [d.strip() for d in data_input.split(",")]
        data.append(row)

    if not validate_input(headers, data):
        print("Error: Number of columns in data rows does not match the number of headers.")
        sys.exit(1)

    if not headers or not data:
        print("No table data to display.")
        sys.exit(1)

    table = create_markdown_table(headers, data)
    print(table)
