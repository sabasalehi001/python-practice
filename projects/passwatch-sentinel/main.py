import json

def calculate_password_strength(password):
    length = len(password)
    has_lower = any(c.islower() for c in password)
    has_upper = any(c.isupper() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_symbol = any(not c.isalnum() for c in password)

    strength = 0
    if length >= 8: strength += 1
    if has_lower: strength += 1
    if has_upper: strength += 1
    if has_digit: strength += 1
    if has_symbol: strength += 1

    return strength


def get_strength_level(strength):
    if strength <= 2:
        return "Weak"
    elif strength <= 4:
        return "Moderate"
    else:
        return "Strong"


def main():
    while True:
        password = input("Enter your password (or type 'exit' to quit): ")
        if password.lower() == 'exit':
            print("Exiting Passwatch Sentinel.")
            break

        if not password:
            print("Password cannot be empty. Please try again.")
            continue

        strength = calculate_password_strength(password)
        level = get_strength_level(strength)

        print(f"Password Strength: {level}")

        if level == "Weak":
            print("Consider using a longer password with a mix of characters.")
        elif level == "Moderate":
            print("Adding more variety could improve the strength.")
        else:
            print("This appears to be a strong password.")

if __name__ == "__main__":
    main()
