import sys

def highlight_text(text, words_to_highlight, color_code='31'):
    """Highlights specified words or phrases within a given text using ANSI escape codes.

    Args:
        text (str): The text to highlight.
        words_to_highlight (list): A list of words or phrases to highlight.
        color_code (str): The ANSI color code to use for highlighting (default: 31 for red).

    Returns:
        str: The highlighted text.
    """
    highlighted_text = text
    for word in words_to_highlight:
        highlighted_text = highlighted_text.replace(word, f'\033[{color_code}m{word}\033[0m')
    return highlighted_text


def reverse_sentence(sentence):
    """Reverses the order of words in a sentence.

    Args:
        sentence (str): The sentence to reverse.

    Returns:
        str: The reversed sentence.
    """
    words = sentence.split()
    reversed_words = words[::-1]
    return ' '.join(reversed_words)


def main():
    """Main function to interact with the user and perform string manipulations."""
    print("Welcome to LexiLuminary!")

    while True:
        print("\nChoose an option:\")
        print("1. Highlight Text")
        print("2. Reverse Sentence")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ")

        if choice == '1':
            text = input("Enter the text: ")
            words_str = input("Enter the words/phrases to highlight (comma-separated): ")
            words_to_highlight = [word.strip() for word in words_str.split(',')]
            if not all(word for word in words_to_highlight): # Check for empty strings
                print("Error: Please provide valid words/phrases to highlight.")
                continue
            highlighted_text = highlight_text(text, words_to_highlight)
            print("Highlighted text:\n", highlighted_text)
        elif choice == '2':
            sentence = input("Enter the sentence: ")
            reversed_sentence = reverse_sentence(sentence)
            print("Reversed sentence:\n", reversed_sentence)
        elif choice == '3':
            print("Exiting LexiLuminary. Goodbye!")
            sys.exit()
        else:
            print("Invalid choice. Please enter a number between 1 and 3.")

if __name__ == "__main__":
    main()
