import json

def validate_input(user_input, expected_type):
    try:
        if expected_type == int:
            int(user_input)
            return True
        return True # For strings, always valid
    except ValueError:
        return False


def run_quiz(flashcards):
    score = 0
    for i, flashcard in enumerate(flashcards):
        print(f"\nQuestion {i+1}: {flashcard['question']}")
        answer = input("Your Answer: ").strip()
        if answer.lower() == flashcard['answer'].lower():
            print("Correct!")
            score += 1
        else:
            print(f"Incorrect. The correct answer is: {flashcard['answer']}")

    print(f"\nQuiz Complete! Your score: {score}/{len(flashcards)}")


if __name__ == "__main__":
    flashcards = [
        {
            "question": "What is the capital of France?",
            "answer": "Paris"
        },
        {
            "question": "What is 2 + 2?",
            "answer": "4"
        },
        {
            "question": "What is the largest planet in our solar system?",
            "answer": "Jupiter"
        }
    ]

    print("Welcome to MemoMaestro!")
    while True:
        start_quiz = input("Start Quiz? (yes/no): ").lower()
        if start_quiz not in ('yes', 'no'):
            print("Invalid input. Please enter 'yes' or 'no'.")
            continue

        if start_quiz == 'yes':
            run_quiz(flashcards)
            break
        elif start_quiz == 'no':
            print("Exiting...")
            break
