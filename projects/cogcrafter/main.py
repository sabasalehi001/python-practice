def ask_question(question, answer):
    """Asks a question and checks the answer."""
    print(question)
    user_answer = input("Your answer: ").strip().lower()
    if user_answer == answer.lower():
        print("Correct!")
        return True
    else:
        print(f"Incorrect. The answer was: {answer}")
        return False


def validate_play_again(choice):
  """Validates play again input."""
  if choice.lower() not in ['y', 'n']:
    print("Invalid input. Please enter 'y' or 'n'.")
    return False
  return True


def main():
    """Main function to run the quiz."""
    print("Welcome to CogCrafter!")
    score = 0

    questions = [
        {
            "question": "Question 1: I am always coming but never arrive. I am always present but never here. What am I?",
            "answer": "The future"
        },
        {
            "question": "Question 2: What has an eye, but cannot see?",
            "answer": "A needle"
        },
        {
            "question": "Question 3: What is full of holes but still holds water?",
            "answer": "A sponge"
        }
    ]

    for q in questions:
        if ask_question(q["question"], q["answer"]):
            score += 1

    print(f"\nQuiz complete! You scored {score} out of {len(questions)}.")

    play_again = input("Play again? (y/n): ")

    while not validate_play_again(play_again):
      play_again = input("Play again? (y/n): ")

    if play_again.lower() == 'y':
      main()
    else:
      print("Thanks for playing!")

if __name__ == "__main__":
    main()
