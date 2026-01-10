def get_table_data():
    """Gets table data from user input."""
    while True:
        headers_str = input("Column headers (comma-separated): ").strip()
        if not headers_str:
            print("Headers cannot be empty.")
            continue
        headers = [h.strip() for h in headers_str.split(',')]
        if any(not h for h in headers):
            print("Headers cannot contain empty strings.")
            continue
        break

    rows = []
    row_num = 1
    while True:
        row_str = input(f"Row {row_num} (or 'done' to finish): ").strip()
        if row_str.lower() == 'done':
            break
        if not row_str:
            print("Row cannot be empty.")
            continue
        row = [d.strip() for d in row_str.split(',')]
        if len(row) != len(headers):
            print(f"Row must have {len(headers)} columns, but has {len(row)}.")
            continue
        rows.append(row)
        row_num += 1

    return headers, rows


def format_markdown_table(headers, rows):
    """Formats data into a Markdown table string."""
    header_row = "| " + " | ".join(headers) + " |\n"
    separator_row = "|" + "------|" * len(headers) + "\n"
    data_rows = ["| " + " | ".join(row) + " |\n" for row in rows]
    return header_row + separator_row + "".join(data_rows)


if __name__ == "__main__":
    headers, rows = get_table_data()
    if headers and rows:
        table = format_markdown_table(headers, rows)
        print("\nMarkdown Table:\n")
        print(table)
    else:
        print("No table data entered.")
