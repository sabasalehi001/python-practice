import json

def caesar_cipher(text, shift, mode):
    result = ''
    for char in text:
        if char.isalpha():
            start = ord('a') if char.islower() else ord('A')
            shifted_char = chr((ord(char) - start + shift) % 26 + start) if mode == 'encrypt' else chr((ord(char) - start - shift) % 26 + start)
        elif char.isdigit():
            shifted_char = str((int(char) + shift) % 10) if mode == 'encrypt' else str((int(char) - shift) % 10)
        else:
            shifted_char = char
        result += shifted_char
    return result


def validate_shift(shift):
    try:
        shift = int(shift)
        return shift
    except ValueError:
        return None


if __name__ == "__main__":
    while True:
        mode = input("Encrypt or decrypt? (encrypt/decrypt/exit): ").lower()
        if mode == 'exit':
            break
        elif mode not in ('encrypt', 'decrypt'):
            print("Invalid mode. Please choose 'encrypt', 'decrypt', or 'exit'.")
            continue

        text = input("Enter the text: ")
        shift_input = input("Enter the shift value (integer): ")

        shift = validate_shift(shift_input)
        if shift is None:
            print("Invalid shift value. Please enter an integer.")
            continue

        result = caesar_cipher(text, shift, mode)
        print("Result:", result)
