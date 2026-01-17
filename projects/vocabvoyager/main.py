import json

def load_flashcards():
    try:
        with open('flashcards.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def save_flashcards(flashcards):
    with open('flashcards.json', 'w') as f:
        json.dump(flashcards, f, indent=4)

def add_flashcard(flashcards):
    word = input("Enter the word: ").strip()
    if not word:
        print("Word cannot be empty.")
        return
    definition = input(f"Enter the definition for '{word}': ").strip()
    if not definition:
        print("Definition cannot be empty.")
        return
    flashcards[word] = definition
    print(f"Flashcard added for '{word}'.")

def run_quiz(flashcards):
    if not flashcards:
        print("No flashcards available. Add some first!")
        return
    score = 0
    total = len(flashcards)
    for word, definition in flashcards.items():
        answer = input(f"What is the definition of '{word}'? ").strip()
        if answer.lower() == definition.lower():
            print("Correct!")
            score += 1
        else:
            print(f"Incorrect. The correct definition was: {definition}")
    print(f"Quiz complete! Your score: {score}/{total}")


if __name__ == "__main__":
    flashcards = load_flashcards()

    while True:
        print("\nOptions:")
        print("1. Add Flashcard")
        print("2. Take Quiz")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ").strip()

        if choice == '1':
            add_flashcard(flashcards)
            save_flashcards(flashcards)
        elif choice == '2':
            run_quiz(flashcards)
        elif choice == '3':
            print("Exiting VocabVoyager.")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")
