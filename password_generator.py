
import string
import secrets

def generate_password(length):
    if length < 8:
        return None

    letters = string.ascii_letters
    numbers = string.digits
    symbols = "!@#$%^&*()-_=+"

    # Ensure every character type is included
    password = [
        secrets.choice(string.ascii_lowercase),
        secrets.choice(string.ascii_uppercase),
        secrets.choice(numbers),
        secrets.choice(symbols)
    ]

    all_characters = letters + numbers + symbols

    password += [
        secrets.choice(all_characters)
        for _ in range(length - 4)
    ]

    secrets.SystemRandom().shuffle(password)
    return "".join(password)


print("=" * 35)
print("      PASSWORD GENERATOR")
print("=" * 35)

try:
    length = int(input("Enter password length (minimum 8): "))

    password = generate_password(length)

    if password:
        print("\nGenerated Password:", password)
        print("Password generated successfully!")
    else:
        print("Please enter at least 8 characters.")

except ValueError:
    print("Invalid input! Enter a number.")
