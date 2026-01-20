import random

def validate_input(user_input, allowed_values):
    """Validates user input against a set of allowed values."""
    if user_input.lower() not in allowed_values:
        print("Invalid input. Please enter one of the following:", ', '.join(allowed_values))
        return False
    return True

def run_quiz(flashcards):
    """Runs the flashcard quiz."""
    score = 0
    card_count = len(flashcards)
    
    if card_count == 0:
        print("No flashcards available. Please add some flashcards to the dictionary.")
        return
    
    questions = list(flashcards.keys())
    random.shuffle(questions)

    for question in questions:
        answer = flashcards[question]
        user_answer = input(f"Question: {question}\nYour Answer: ").strip()

        if user_answer.lower() == answer.lower():
            print("Correct!")
            score += 1
        else:
            print(f"Incorrect. The correct answer is: {answer}")

    print(f"\nQuiz complete! You scored {score} out of {card_count}.")


if __name__ == "__main__":
    flashcards = {
        "What is the capital of France?": "Paris",
        "What is 2 + 2?": "4",
        "What is the chemical symbol for water?": "H2O",
        "Who painted the Mona Lisa?": "Leonardo da Vinci"
    }

    while True:
        print("\nWelcome to CranialCartographer!")
        print("1. Start Quiz")
        print("2. Exit")

        choice = input("Enter your choice (1 or 2): ")

        if not validate_input(choice, ['1', '2']):
            continue

        if choice == '1':
            run_quiz(flashcards)
        elif choice == '2':
            print("Exiting...")
            break
