import sys

def caesar_cipher(text, key, mode):
    result = ''
    for char in text:
        if char.isalpha():
            start = ord('a') if char.islower() else ord('A')
            shifted_char = chr((ord(char) - start + key * mode) % 26 + start)
        else:
            shifted_char = char
        result += shifted_char
    return result


def get_user_input(prompt, validation_func=None):
    while True:
        value = input(prompt).strip()
        if validation_func is None or validation_func(value):
            return value
        else:
            print("Invalid input. Please try again.")


def validate_integer(value):
    try:
        int(value)
        return True
    except ValueError:
        return False


if __name__ == "__main__":
    print("\nWelcome to WhisperWeave - A Simple Caesar Cipher Tool\n")

    while True:
        action = get_user_input("Choose an action (encrypt/decrypt/exit): ").lower()
        if action not in ['encrypt', 'decrypt', 'exit']:
            print("Invalid action. Please choose 'encrypt', 'decrypt', or 'exit'.")
            continue

        if action == 'exit':
            print("Exiting WhisperWeave.")
            sys.exit()

        text = get_user_input("Enter the text: ")
        key_str = get_user_input("Enter the key (integer): ", validate_integer)
        key = int(key_str)

        if action == 'encrypt':
            encrypted_text = caesar_cipher(text, key, 1)
            print("Encrypted text:", encrypted_text)
        elif action == 'decrypt':
            decrypted_text = caesar_cipher(text, key, -1)
            print("Decrypted text:", decrypted_text)

        print()
