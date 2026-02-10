def get_integer_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
            else:
                print("Please enter a positive integer.")
        except ValueError:
            print("Invalid input. Please enter an integer.")


def create_table(num_cols, headers, data):
    header_row = "| " + " | ".join(headers) + " |\n"
    separator_row = "|" + "------|" * num_cols + "\n"
    data_rows = []
    for row in data:
        data_rows.append("| " + " | ".join(row) + " |\n")
    return header_row + separator_row + "".join(data_rows)


if __name__ == "__main__":
    num_cols = get_integer_input("Number of columns: ")

    headers = []
    for i in range(num_cols):
        header = input(f"Column {i + 1} header: ")
        headers.append(header)

    num_rows = get_integer_input("Number of rows: ")

    data = []
    for i in range(num_rows):
        row_data = []
        for j in range(num_cols):
            cell_data = input(f"Row {i + 1}, Column {j + 1}: ")
            row_data.append(cell_data)
        data.append(row_data)

    markdown_table = create_table(num_cols, headers, data)
    print(markdown_table)
