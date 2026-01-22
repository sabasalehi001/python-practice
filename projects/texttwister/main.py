import sys

def reverse_string(text):
    """Reverses a string."""
    return text[::-1]

def alternate_case(text):
    """Converts a string to alternating case."""
    result = ''
    for i, char in enumerate(text):
        if i % 2 == 0:
            result += char.upper()
        else:
            result += char.lower()
    return result

def is_palindrome(text):
    """Checks if a string is a palindrome (case-insensitive)."""
    processed_text = ''.join(filter(str.isalnum, text)).lower()
    return processed_text == processed_text[::-1]


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python main.py <command> <string>")
        sys.exit(1)

    command = sys.argv[1].lower()
    text = sys.argv[2]

    if not isinstance(text, str):
        print("Error: Input must be a string.")
        sys.exit(1)

    if command == "reverse":
        print(reverse_string(text))
    elif command == "alternate":
        print(alternate_case(text))
    elif command == "palindrome":
        print(is_palindrome(text))
    else:
        print("Error: Invalid command. Available commands: reverse, alternate, palindrome")
        sys.exit(1)
