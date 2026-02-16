import random

def validate_input(user_input):
    """Validates user input to ensure it's not empty."""
    if not user_input.strip():
        return False
    return True

def run_quiz(flashcards):
    """Runs the flashcard quiz."""
    score = 0
    for definition, word in flashcards.items():
        print(f"Definition: {definition}")
        user_answer = input("Your answer: ").strip().lower()

        if not validate_input(user_answer):
            print("Invalid input. Please provide an answer.")
            continue

        if user_answer == word.lower():
            print("Correct!")
            score += 1
        else:
            print(f"Incorrect. The correct answer is: {word}")

    print(f"\nQuiz complete! Your score: {score}/{len(flashcards)}")

if __name__ == "__main__":
    flashcards = {
        "A large body of water surrounded by land": "Lake",
        "A tall, natural elevation of the earth's surface": "Mountain",
        "A stream of water flowing in a channel to the sea, a lake, or another stream": "River",
        "An extensive area of treeless grassland": "Prairie",
        "A piece of land almost surrounded by water or projecting out into a body of water": "Peninsula"
    }

    # Shuffle the flashcards to randomize the quiz
    items = list(flashcards.items())
    random.shuffle(items)
    flashcards = dict(items)

    print("Welcome to LexiLantern! Let's test your vocabulary.")
    run_quiz(flashcards)
