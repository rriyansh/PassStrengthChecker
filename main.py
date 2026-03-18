
import re
import random
import string
import math


def check_password_strength(password):
    score = 0

    if len(password) >= 8:
        score += 1
    if re.search(r"[A-Z]", password):
        score += 1
    if re.search(r"[a-z]", password):
        score += 1
    if re.search(r"[0-9]", password):
        score += 1
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1

    if score <= 2:
        return "Weak 🔴"
    elif score <= 4:
        return "Medium 🟡"
    else:
        return "Strong 🟢"


def get_feedback(password):
    feedback = []

    if len(password) < 8:
        feedback.append("• Password should be at least 8 characters long")
    if not re.search(r"[A-Z]", password):
        feedback.append("• Add at least one uppercase letter")
    if not re.search(r"[a-z]", password):
        feedback.append("• Add at least one lowercase letter")
    if not re.search(r"[0-9]", password):
        feedback.append("• Include at least one number")
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        feedback.append("• Include at least one special character")

    return feedback


def generate_strong_password():
    characters = string.ascii_letters + string.digits + "!@#$%^&*"
    return ''.join(random.choice(characters) for _ in range(12))


def calculate_entropy(password):
    charset = 0

    if re.search(r"[a-z]", password):
        charset += 26
    if re.search(r"[A-Z]", password):
        charset += 26
    if re.search(r"[0-9]", password):
        charset += 10
    if re.search(r"[!@#$%^&*]", password):
        charset += 32

    if charset == 0:
        return 0

    entropy = len(password) * math.log2(charset)
    return round(entropy, 2)


def time_to_crack(entropy):
    guesses_per_second = 1e9
    seconds = (2 ** entropy) / guesses_per_second
    return round(seconds, 2)


def main():
    print("🔐 Password Strength Checker (Advanced)\n")

    while True:
        password = input("Enter your password (or type 'exit'): ")

        if password.lower() == "exit":
            print("Goodbye 👋")
            break

        strength = check_password_strength(password)
        entropy = calculate_entropy(password)

        print("\nPassword Strength:", strength)
        print("Entropy:", entropy)
        print("Estimated Crack Time (seconds):", time_to_crack(entropy))

        feedback = get_feedback(password)
        if feedback:
            print("\nSuggestions:")
            for f in feedback:
                print(f)

        if strength == "Weak 🔴":
            print("\nSuggested Strong Password:", generate_strong_password())


if __name__ == "__main__":
    main()
