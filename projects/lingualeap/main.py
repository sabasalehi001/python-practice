import json

def add_flashcard(flashcards):
    term = input("Enter the term (e.g., English word): ").strip()
    definition = input("Enter the definition (e.g., Spanish translation): ").strip()
    if not term or not definition:
        print("Term and definition cannot be empty.")
        return flashcards
    flashcards[term] = definition
    print("Flashcard added!")
    return flashcards

def run_quiz(flashcards):
    if not flashcards:
        print("No flashcards available. Add some first!")
        return
    
    correct_count = 0
    total_count = len(flashcards)

    for term, definition in flashcards.items():
        answer = input(f"What is the definition of '{term}'? ").strip()
        if answer.lower() == definition.lower():
            print("Correct!")
            correct_count += 1
        else:
            print(f"Incorrect. The correct answer is '{definition}'.")

    print(f"Quiz complete! You got {correct_count} out of {total_count} correct.")


def main():
    flashcards = {}

    while True:
        print("\nLinguaLeap: Flashcard Quiz")
        print("1. Add Flashcard")
        print("2. Start Quiz")
        print("3. Quit")

        choice = input("Enter your choice: ").strip()

        if choice == '1':
            flashcards = add_flashcard(flashcards)
        elif choice == '2':
            run_quiz(flashcards)
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
