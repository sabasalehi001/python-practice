morse_code = {
    '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E',
    '..-.': 'F', '--.': 'G', '....': 'H', '..': 'I', '.---': 'J',
    '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O',
    '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T',
    '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y',
    '--..': 'Z', '-----': '0', '.----': '1', '..---': '2',
    '...--': '3', '....-': '4', '.....': '5', '-....': '6',
    '--...': '7', '---..': '8', '----.': '9',
    '.-.-.-': '.', '--..--': ',', '..--..': '?', '.----.': "'",
    '-.-.--': '!', '-..-.': '/', '-.--.': '(', '-.--.-': ')',
    '.-...': '&', '---...': ':', '-.-.-.': ';', '-...-': '=',
    '.-.-.': '+', '-....-': '-', '..--.-': '_', '.-..-.': '"',
    '.--.-.': '@'
}

def decode_letter(letter):
    if letter in morse_code:
        return morse_code[letter]
    else:
        return ''

def decode_message(message):
    words = message.split(' / ')
    decoded_words = []
    for word in words:
        letters = word.split(' ')
        decoded_letters = []
        for letter in letters:
            decoded_letters.append(decode_letter(letter))
        decoded_words.append(''.join(decoded_letters))
    return ' '.join(decoded_words).upper()

def validate_morse(morse_code_input):
    valid_chars = ['.', '-', ' ', '/']
    for char in morse_code_input:
        if char not in valid_chars:
            return False
    return True

if __name__ == "__main__":
    while True:
        morse_input = input("Enter Morse code (separate letters with space, words with '/'): ")
        if not validate_morse(morse_input):
            print("Invalid Morse code input. Please use only '.', '-', ' ', and '/'.")
            continue

        if not morse_input:
            print("Please enter some Morse code.")
            continue

        decoded_message = decode_message(morse_input)
        print("Output:", decoded_message)
        break
