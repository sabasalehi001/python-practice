import sys

rune_map = {
    'a': 'ᚨ', 'b': 'ᛒ', 'c': 'ᚲ', 'd': 'ᛞ', 'e': 'ᛂ', 'f': 'ᚠ',
    'g': 'ᚷ', 'h': 'ᚺ', 'i': 'ᛁ', 'j': 'ᛃ', 'k': 'ᚲ', 'l': 'ᛚ',
    'm': 'ᛗ', 'n': 'ᚾ', 'o': 'ᛟ', 'p': 'ᛈ', 'q': 'ᚲ', 'r': 'ᚱ',
    's': 'ᛊ', 't': 'ᛏ', 'u': 'ᚢ', 'v': 'ᚹ', 'w': 'ᚹ', 'x': 'ᛪ',
    'y': 'ᛦ', 'z': 'ᛉ'
}

def encrypt(text):
    """Encrypts text using the rune substitution cipher."""
    encrypted_text = ''
    for char in text.lower():
        if char in rune_map:
            encrypted_text += rune_map[char]
        else:
            encrypted_text += char  # Keep characters not in the map as is
    return encrypted_text

def decrypt(text):
    """Decrypts text using the rune substitution cipher."""
    decrypted_text = ''
    reverse_rune_map = {v: k for k, v in rune_map.items()}
    for char in text:
        if char in reverse_rune_map:
            decrypted_text += reverse_rune_map[char]
        else:
            decrypted_text += char  # Keep characters not in the map as is
    return decrypted_text

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python main.py (encrypt|decrypt) <text>")
        sys.exit(1)

    action = sys.argv[1].lower()
    text = sys.argv[2]

    if action == "encrypt":
        result = encrypt(text)
        print(result)
    elif action == "decrypt":
        result = decrypt(text)
        print(result)
    else:
        print("Invalid action. Use 'encrypt' or 'decrypt'.")
        sys.exit(1)
