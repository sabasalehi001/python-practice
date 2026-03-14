def caesar_cipher(text, shift, mode):
    """Encrypts or decrypts text using a Caesar cipher."""
    result = ''
    for char in text:
        if char.isalpha():
            start = ord('a') if char.islower() else ord('A')
            shifted_char = chr((ord(char) - start + shift) % 26 + start) if mode == 'encrypt' else chr((ord(char) - start - shift) % 26 + start)
        else:
            shifted_char = char
        result += shifted_char
    return result


def get_user_input():
    """Gets user input for the cipher operation."""
    while True:
        mode = input("Choose an operation (encrypt/decrypt): ").lower()
        if mode in ['encrypt', 'decrypt']:
            break
        else:
            print("Invalid operation. Please choose 'encrypt' or 'decrypt'.")

    text = input("Enter text: ")

    while True:
        try:
            shift = int(input("Enter shift value (integer): "))
            break
        except ValueError:
            print("Invalid shift value. Please enter an integer.")

    return mode, text, shift


if __name__ == "__main__":
    mode, text, shift = get_user_input()
    encrypted_text = caesar_cipher(text, shift, mode)
    print(f"{mode.capitalize()}ed text: {encrypted_text}")
