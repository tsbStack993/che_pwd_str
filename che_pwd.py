import re
from datetime import datetime

# Expanded common password list for better security
COMMON_PASSWORDS = {
    "password", "123456", "qwerty", "12345678", "abc123", "password1",
    "111111", "123456789", "12345", "123123", "qwertyuiop", "letmein",
    "welcome", "monkey", "dragon", "football", "iloveyou", "admin"
}

def check_password_strength(password):
    """Evaluate password against security standards and provide suggestions."""
    length = len(password) >= 8
    uppercase = bool(re.search(r'[A-Z]', password))
    lowercase = bool(re.search(r'[a-z]', password))
    digit = bool(re.search(r'\d', password))
    special = bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))
    not_common = password.lower() not in COMMON_PASSWORDS

    criteria = [length, uppercase, lowercase, digit, special, not_common]
    strength = sum(criteria)

    # Suggestions for improvement
    suggestions = []
    if not length:
        suggestions.append("Use at least 8 characters.")
    if not uppercase:
        suggestions.append("Add uppercase letters (A-Z).")
    if not lowercase:
        suggestions.append("Add lowercase letters (a-z).")
    if not digit:
        suggestions.append("Include numbers (0-9).")
    if not special:
        suggestions.append("Add special characters (e.g., !@#$%).")
    if not not_common:
        suggestions.append("Avoid common passwords like 'password', '123456', or 'qwerty'.")
    if strength >= 5:
        suggestions.append("Great job! Your password is strong.")

    # Generate security report
    report = {
        "password": password,
        "strength": f"{strength}/6",
        "is_strong": strength >= 5,
        "length": length,
        "uppercase": uppercase,
        "lowercase": lowercase,
        "digit": digit,
        "special": special,
        "not_common": not_common,
        "suggestions": suggestions,
        "timestamp": datetime.now().isoformat()
    }
    return report

if __name__ == "__main__":
    # Accept user input and check password strength
    user_password = input("Enter your password: ")
    result = check_password_strength(user_password)
    # Display result
    print("Password Strength Report:")
    print(f"Strength: {result['strength']} ({'Strong' if result['is_strong'] else 'Weak'})")
    print("Criteria met:")
    print(f"  Length >= 8: {result['length']}")
    print(f"  Uppercase: {result['uppercase']}")
    print(f"  Lowercase: {result['lowercase']}")
    print(f"  Digit: {result['digit']}")
    print(f"  Special: {result['special']}")
    print(f"  Not common: {result['not_common']}")
    print("Suggestions:")
    for s in result["suggestions"]:
        print(f"  - {s}")
    print(f"Checked at: {result['timestamp']}")