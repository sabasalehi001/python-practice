MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---',
    '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..',
    '9': '----.', ' ': '/' 
}

def text_to_morse(text):
    morse_code = ''
    for char in text.upper():
        if char in MORSE_CODE_DICT:
            morse_code += MORSE_CODE_DICT[char] + ' '
        else:
            pass # Ignore unsupported characters
    return morse_code.strip()

def morse_to_text(morse_code):
    reverse_morse_dict = {v: k for k, v in MORSE_CODE_DICT.items()}
    text = ''
    words = morse_code.split('/')
    for word in words:
        chars = word.split()
        for char in chars:
            if char in reverse_morse_dict:
                text += reverse_morse_dict[char]
            else:
                pass #Ignore invalid morse
        text += ' '
    return text.strip()

def validate_input(choice):
    if choice not in ['1', '2']:
        return False
    return True

if __name__ == '__main__':
    while True:
        print("\nChoose translation direction:")
        print("1. Text to Morse code")
        print("2. Morse code to Text")
        print("3. Exit")

        choice = input("Enter your choice (1 or 2 or 3): ")
        
        if choice == '3':
            break

        if not validate_input(choice) and choice != '3':
            print("Invalid choice. Please enter 1, 2, or 3.")
            continue

        if choice == '1':
            text = input("Enter the text to translate: ")
            morse = text_to_morse(text)
            print("Morse code:", morse)
        elif choice == '2':
            morse = input("Enter the Morse code to translate (use '.' for dot, '-' for dash, '/' for space between words): ")
            text = morse_to_text(morse)
            print("Text:", text)
