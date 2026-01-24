import json

def load_flashcards():
    try:
        with open('flashcards.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("Error: flashcards.json is corrupted. Starting with empty list.")
        return []

def save_flashcards(flashcards):
    with open('flashcards.json', 'w') as f:
        json.dump(flashcards, f, indent=4)


def add_flashcard(flashcards):
    term = input("Enter the term: ")
    definition = input("Enter the definition: ")
    flashcards.append({'term': term, 'definition': definition})
    print("Flashcard added!")


def take_quiz(flashcards):
    if not flashcards:
        print("No flashcards available. Add some first!")
        return

    score = 0
    for flashcard in flashcards:
        answer = input(f"What is the definition of '{flashcard['term']}'? ")
        if answer.lower() == flashcard['definition'].lower():
            print("Correct!")
            score += 1
        else:
            print(f"Incorrect. The correct answer was: {flashcard['definition']}")

    print(f"Quiz complete! Your score: {score}/{len(flashcards)}")


def main():
    flashcards = load_flashcards()

    while True:
        print("\nOptions:")
        print("1. Add flashcard")
        print("2. Take quiz")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ")

        if choice == '1':
            add_flashcard(flashcards)
            save_flashcards(flashcards)
        elif choice == '2':
            take_quiz(flashcards)
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 3.")

if __name__ == "__main__":
    main()
