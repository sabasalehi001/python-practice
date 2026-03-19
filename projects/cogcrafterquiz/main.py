def is_integer(value):
    try:
        int(value)
        return True
    except ValueError:
        return False

def run_quiz():
    questions = [
        {
            "question": "I am a number that is greater than 10 and less than 20. I am odd and divisible by 3. What number am I?",
            "answer": "15"
        },
        {
            "question": "What has an eye, but cannot see?",
            "answer": "needle"
        },
        {
            "question": "What is always in front of you but can’t be seen?",
            "answer": "future"
        }
    ]

    score = 0
    for i, q in enumerate(questions):
        print(f"\nQuestion {i + 1}: {q['question']}")
        user_answer = input("Your answer: ").strip().lower()

        if user_answer == q['answer'].lower():
            print("Correct!")
            score += 1
        else:
            print(f"Incorrect. The answer is: {q['answer']}")

    print(f"\nQuiz complete! Your score: {score}/{len(questions)}")


if __name__ == "__main__":
    print("Welcome to CogCrafterQuiz!")
    while True:
        start = input("Start quiz? (yes/no): ").strip().lower()
        if start == 'yes':
            run_quiz()
            break
        elif start == 'no':
            print("Exiting.")
            break
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")
