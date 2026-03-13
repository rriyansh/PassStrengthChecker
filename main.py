import re

def check_password_strength(password):
    score = 0

    # Length check
    if len(password) >= 8:
        score += 1

    # Uppercase check
    if re.search(r"[A-Z]", password):
        score += 1

    # Lowercase check
    if re.search(r"[a-z]", password):
        score += 1

    # Number check
    if re.search(r"[0-9]", password):
        score += 1

    # Special character check
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1

    if score <= 2:
        return "Weak 🔴"
    elif score == 3 or score == 4:
        return "Medium 🟡"
    else:
        return "Strong 🟢"


password = input("Enter your password: ")
strength = check_password_strength(password)

print("Password Strength:", strength)
