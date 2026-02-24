def caesar_cipher(text, shift, mode):
    result = ''
    for char in text:
        if char.isalpha():
            start = ord('a') if char.islower() else ord('A')
            shifted_char = chr((ord(char) - start + shift) % 26 + start) if mode == 'encrypt' else chr((ord(char) - start - shift) % 26 + start)
        else:
            shifted_char = char
        result += shifted_char
    return result

def validate_shift(shift):
    try:
        shift_value = int(shift)
        return shift_value
    except ValueError:
        return None


if __name__ == "__main__":
    while True:
        operation = input("Choose an operation (encrypt/decrypt): ").lower()
        if operation not in ['encrypt', 'decrypt']:
            print("Invalid operation. Please choose 'encrypt' or 'decrypt'.")
            continue

        text = input("Enter the text: ")
        shift = input("Enter the shift value: ")

        shift_value = validate_shift(shift)

        if shift_value is None:
            print("Invalid shift value. Please enter an integer.")
            continue

        if operation == 'encrypt':
            ciphertext = caesar_cipher(text, shift_value, 'encrypt')
            print("Ciphertext:", ciphertext)
        else:
            plaintext = caesar_cipher(text, shift_value, 'decrypt')
            print("Plaintext:", plaintext)

        another = input("Do you want to perform another operation? (yes/no): ").lower()
        if another != 'yes':
            break
