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


def get_user_input(prompt, data_type, validation_func=None):
    while True:
        user_input = input(prompt)
        try:
            converted_input = data_type(user_input)
            if validation_func is None or validation_func(converted_input):
                return converted_input
            else:
                print("Invalid input. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a valid value.")

if __name__ == "__main__":
    print("Welcome to CipherCrate!")

    while True:
        mode = input("Do you want to encrypt or decrypt? (encrypt/decrypt/exit): ").lower()

        if mode == 'exit':
            break
        elif mode not in ('encrypt', 'decrypt'):
            print("Invalid mode. Please choose 'encrypt', 'decrypt', or 'exit'.")
            continue

        text = input("Enter the text: ")

        shift = get_user_input("Enter the shift value (integer): ", int, lambda x: -26 <= x <= 26)

        result = caesar_cipher(text, shift, mode)

        print("Result:", result)
