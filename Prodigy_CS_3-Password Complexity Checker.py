import re

def check_password_strength(password):
    # Initialize variables to check the criteria
    length = len(password) >= 8
    has_upper = bool(re.search(r'[A-Z]', password))
    has_lower = bool(re.search(r'[a-z]', password))
    has_digit = bool(re.search(r'\d', password))
    has_special = bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))

    # Calculate strength score
    strength_score = sum([length, has_upper, has_lower, has_digit, has_special])

    # Provide feedback based on the strength score
    if strength_score == 5:
        feedback = "Very Strong"
    elif strength_score == 4:
        feedback = "Strong"
    elif strength_score == 3:
        feedback = "Moderate"
    elif strength_score == 2:
        feedback = "Weak"
    else:
        feedback = "Very Weak"

    # Detail the criteria for the user
    criteria = {
        "Length (>= 8 characters)": length,
        "Uppercase letters (A-Z)": has_upper,
        "Lowercase letters (a-z)": has_lower,
        "Numbers (0-9)": has_digit,
        "Special characters": has_special
    }

    return feedback, criteria

def main():
    password = input("Enter a password to check its strength: ")
    feedback, criteria = check_password_strength(password)

    print(f"\nPassword Strength: {feedback}\n")
    print("Criteria met:")
    for criterion, met in criteria.items():
        status = "??" if met else "?"
        print(f"{status} {criterion}")

if _name_ == "_main_":
    main()