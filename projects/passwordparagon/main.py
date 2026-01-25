import re

def calculate_strength(password):
    """Calculates password strength based on length and character types."""
    length = len(password)
    has_upper = bool(re.search(r'[A-Z]', password))
    has_lower = bool(re.search(r'[a-z]', password))
    has_digit = bool(re.search(r'[0-9]', password))
    has_symbol = bool(re.search(r'[^a-zA-Z0-9]', password))

    strength = 0
    if length >= 8: strength += 1
    if has_upper: strength += 1
    if has_lower: strength += 1
    if has_digit: strength += 1
    if has_symbol: strength += 1

    return strength


def get_rating(strength):
    """Returns a password strength rating based on the calculated strength score."""
    if strength <= 1:
        return "Weak"
    elif strength <= 3:
        return "Moderate"
    elif strength <= 4:
        return "Strong"
    else:
        return "Excellent"


if __name__ == "__main__":
    while True:
        password = input("Enter your password (or type 'exit' to quit): ")
        if password.lower() == 'exit':
            break

        if not password:
            print("Password cannot be empty. Please try again.")
            continue

        strength = calculate_strength(password)
        rating = get_rating(strength)

        print(f"Password Strength: {rating}")

        if rating == "Weak":
            print("Suggestion: Use a longer password with a mix of character types.")
        elif rating == "Moderate":
            print("Suggestion: Add more symbols or numbers.")
        elif rating == "Strong":
            print("Suggestion: Consider adding more diversity in characters for even greater security.")
        else:
            print("Your password is very strong!")
