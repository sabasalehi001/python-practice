import sys

def rgb_to_hex(rgb):
    """Converts an RGB tuple to a Hex color code."""
    try:
        r, g, b = map(int, rgb.split(','))
        if not all(0 <= x <= 255 for x in [r, g, b]):
            raise ValueError
        return '#{:02X}{:02X}{:02X}'.format(r, g, b)
    except ValueError:
        return None

def hex_to_rgb(hex_code):
    """Converts a Hex color code to an RGB tuple."""
    hex_code = hex_code.lstrip('#')
    if len(hex_code) != 6:
        return None
    try:
        r = int(hex_code[0:2], 16)
        g = int(hex_code[2:4], 16)
        b = int(hex_code[4:6], 16)
        return (r, g, b)
    except ValueError:
        return None


def main():
    """Main function to handle user input and color conversion."""
    print("Choose conversion direction:")
    print("1. RGB to Hex")
    print("2. Hex to RGB")

    choice = input("> ")

    if choice == '1':
        rgb = input("Enter RGB values (comma-separated, e.g., 255,0,102): ")
        hex_code = rgb_to_hex(rgb)
        if hex_code:
            print("Hex code:", hex_code)
        else:
            print("Invalid RGB input. Please enter comma separated values between 0 and 255.")
    elif choice == '2':
        hex_code = input("Enter Hex code (e.g., #FF0000): ")
        rgb = hex_to_rgb(hex_code)
        if rgb:
            print("RGB values:", rgb)
        else:
            print("Invalid Hex code. Please enter a valid 6-digit hex code.")
    else:
        print("Invalid choice. Please select 1 or 2.")

if __name__ == "__main__":
    main()
