import sys

def get_header():
    header_input = input("Enter the table headers, separated by commas: ")
    headers = [h.strip() for h in header_input.split(',')]
    if not all(headers): # Check for empty strings
        print("Error: Headers cannot be empty.")
        sys.exit(1)
    return headers

def get_rows(num_cols):
    rows = []
    while True:
        row_input = input("Enter a row of data, separated by commas (or type 'done'): ")
        if row_input.lower() == 'done':
            break
        row_data = [d.strip() for d in row_input.split(',')]
        if len(row_data) != num_cols:
            print(f"Error: Row must have {num_cols} columns.")
            continue
        rows.append(row_data)
    return rows

def generate_markdown_table(headers, rows):
    markdown = "| " + " | ".join(headers) + " |\n"
    markdown += "|" + "---" * len(headers) + "|\n"
    for row in rows:
        markdown += "| " + " | ".join(row) + " |\n"
    return markdown

if __name__ == "__main__":
    try:
        headers = get_header()
        rows = get_rows(len(headers))
        
        if not rows:
          print("No data entered. Exiting.")
          sys.exit(0)

        table = generate_markdown_table(headers, rows)
        print(table)
    except KeyboardInterrupt:
        print("\nExiting.")
        sys.exit(0)
