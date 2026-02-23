def ask_riddle(riddle, answer):
    """Asks a riddle and checks the answer."""
    print(riddle)
    user_answer = input("Your answer: ").strip().lower()
    if user_answer == answer.lower():
        print("Correct!")
        return True
    else:
        print(f"Incorrect. The answer was: {answer}")
        return False


def main():
    """Main function to run the quiz."""
    score = 0
    num_questions = 0

    riddles = {
        "I am taken from a mine, and shut up in a wooden case, from which I am never released, and used by almost everybody. What am I?": "Pencil lead",
        "What has an eye, but cannot see?": "A needle",
        "What is always in front of you but can’t be seen?": "The future",
        "What has to be broken before you can use it?": "An egg",
        "What is full of holes but still holds water?": "A sponge"
    }

    print("Welcome to RiddleRealmRunner!")

    for riddle, answer in riddles.items():
        num_questions += 1
        if ask_riddle(riddle, answer):
            score += 1

    if num_questions > 0:
      print(f"\nQuiz complete! You scored {score} out of {num_questions}.")
    else:
      print("No riddles available.")

if __name__ == "__main__":
    main()
