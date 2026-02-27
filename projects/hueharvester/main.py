import sys

def hex_to_rgb(hex_color):
    hex_color = hex_color.lstrip('#')
    if len(hex_color) != 6:
        return None
    try:
        return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
    except ValueError:
        return None

def rgb_to_hex(rgb_color):
    try:
        r, g, b = map(int, rgb_color)
        if not all(0 <= x <= 255 for x in (r, g, b)):
            return None
        return '#{:02x}{:02x}{:02x}'.format(r, g, b)
    except ValueError:
        return None


def main():
    print("Choose conversion type:")
    print("1. Hex to RGB")
    print("2. RGB to Hex")
    choice = input("Enter your choice (1 or 2): ")

    if choice == '1':
        hex_color = input("Enter hex color code (e.g., #FFFFFF): ")
        rgb = hex_to_rgb(hex_color)
        if rgb:
            print("RGB:", rgb)
        else:
            print("Invalid hex color code.")
    elif choice == '2':
        rgb_color = input("Enter RGB values (e.g., 255,0,0): ")
        rgb_values = rgb_color.split(',')
        if len(rgb_values) != 3:
            print("Invalid RGB format. Please use comma-separated values.")
            return
        hex_color = rgb_to_hex(rgb_values)
        if hex_color:
            print("Hex:", hex_color)
        else:
            print("Invalid RGB values.")
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()
