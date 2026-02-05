def rgb_to_hex(r, g, b):
    """Converts RGB values to a hexadecimal color code."""
    return '#{:02X}{:02X}{:02X}'.format(r, g, b)


def hex_to_rgb(hex_code):
    """Converts a hexadecimal color code to RGB values."""
    hex_code = hex_code.lstrip('#')
    if len(hex_code) != 6:
        raise ValueError("Invalid hex code. Must be 6 characters long.")
    try:
        r = int(hex_code[0:2], 16)
        g = int(hex_code[2:4], 16)
        b = int(hex_code[4:6], 16)
        return (r, g, b)
    except ValueError:
        raise ValueError("Invalid hex characters.")


if __name__ == "__main__":
    while True:
        print("Choose conversion type:")
        print("1. RGB to Hex")
        print("2. Hex to RGB")
        choice = input("Enter your choice (1 or 2): ")

        if choice == '1':
            try:
                rgb_input = input("Enter RGB values (e.g., 255,0,100): ")
                r, g, b = map(int, rgb_input.split(','))
                if not all(0 <= x <= 255 for x in [r, g, b]):
                    print("Error: RGB values must be between 0 and 255.")
                    continue
                hex_code = rgb_to_hex(r, g, b)
                print("Hex code:", hex_code)
                break
            except ValueError:
                print("Error: Invalid RGB input. Please use the format 255,0,100.")

        elif choice == '2':
            try:
                hex_input = input("Enter Hex code (e.g., #FFFFFF): ")
                rgb_values = hex_to_rgb(hex_input)
                print("RGB values:", rgb_values)
                break
            except ValueError as e:
                print("Error:", e)

        else:
            print("Invalid choice. Please enter 1 or 2.")
