import sys

def caesar_cipher(text, shift, mode):
    result = ''
    for char in text:
        if char.isalpha():
            start = ord('a') if char.islower() else ord('A')
            shifted_char = chr((ord(char) - start + shift) % 26 + start) if mode == 'encrypt' else chr((ord(char) - start - shift) % 26 + start)
            result += shifted_char
        else:
            result += char
    return result


def main():
    print("CipherCaddy - Caesar Cipher Tool")

    while True:
        action = input("Encrypt or Decrypt (e/d)? Or Exit (x): ").lower()
        if action in ('e', 'd', 'x'):
            break
        else:
            print("Invalid choice. Please enter 'e', 'd', or 'x'.")

    if action == 'x':
        print("Exiting CipherCaddy.")
        sys.exit()

    text = input("Enter the text: ")

    while True:
        try:
            shift = int(input("Enter the shift value (integer): "))
            break
        except ValueError:
            print("Invalid input. Please enter an integer.")

    mode = 'encrypt' if action == 'e' else 'decrypt'

    result = caesar_cipher(text, shift, mode)
    print("Result:", result)

if __name__ == "__main__":
    main()
