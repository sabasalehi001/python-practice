import random

def validate_answer(answer):
    """Validates that the answer is not empty."""
    if not answer:
        print("Answer cannot be empty. Please try again.")
        return False
    return True

def run_quiz(flashcards):
    """Runs the flashcard quiz."""
    score = 0
    random.shuffle(flashcards)

    for question, answer in flashcards:
        print(f"Question: {question}")
        user_answer = input("Your Answer: ").strip()

        if not validate_answer(user_answer):
            continue

        if user_answer.lower() == answer.lower():
            print("Correct!")
            score += 1
        else:
            print(f"Incorrect. The correct answer is: {answer}")

    print("\nQuiz Complete!")
    print(f"You scored {score} out of {len(flashcards)}.")


if __name__ == "__main__":
    flashcards = [
        ("What is the capital of France?", "Paris"),
        ("What is 2 + 2?", "4"),
        ("What color is the sky?", "Blue"),
        ("What is the chemical symbol for water?", "H2O"),
        ("Who painted the Mona Lisa?", "Leonardo da Vinci")
    ]

    print("Welcome to QuizzicalQuokka!")
    run_quiz(flashcards)
    print("Thanks for playing!")
