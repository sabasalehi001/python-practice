MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..',
    '9': '----.', '0': '-----', ', ': '--..--', '.': '.-.-.-', '?': '..--..',
    '/': '-..-.', '-': '-....-', '(': '-.--.', ')': '-.--.-'
}


def encode_text(text):
    """Encodes English text to Morse code."""
    encoded_text = ''
    for char in text.upper():
        if char != ' ':
            if char in MORSE_CODE_DICT:
                encoded_text += MORSE_CODE_DICT[char] + ' '
            else:
                print(f"Warning: Character '{char}' not found in Morse code dictionary.")
        else:
            encoded_text += '/ '
    return encoded_text.strip()


def decode_morse(morse_code):
    """Decodes Morse code to English text."""
    morse_code_dict_reversed = {value: key for key, value in MORSE_CODE_DICT.items()}
    words = morse_code.split('/ ')
    decoded_text = ''
    for word in words:
        chars = word.split(' ')
        for char in chars:
            if char in morse_code_dict_reversed:
                decoded_text += morse_code_dict_reversed[char]
            else:
                print(f"Warning: Morse code '{char}' not found in dictionary.")
        decoded_text += ' '
    return decoded_text.strip()


if __name__ == "__main__":
    while True:
        mode = input("Choose mode (encode/decode): ").lower()
        if mode not in ['encode', 'decode']:
            print("Invalid mode. Please choose 'encode' or 'decode'.")
            continue

        if mode == 'encode':
            text = input("Enter text: ")
            encoded_text = encode_text(text)
            print(encoded_text)
        else:
            morse_code = input("Enter Morse code: ")
            decoded_text = decode_morse(morse_code)
            print(decoded_text)

        another = input("Translate another? (yes/no): ").lower()
        if another != 'yes':
            break
