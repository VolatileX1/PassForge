import random
import string

def generate_password(length=12, include_digits=True, include_punctuation=True):
    """Generate a random password with customizable options"""
    characters = string.ascii_letters
    if include_digits:
        characters += string.digits
    if include_punctuation:
        characters += string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def check_password_strength(password):
    """Check the strength of a password and rate it as weak, medium, or strong"""
    rating = 0
    if len(password) >= 8:
        rating += 1
    if any(c.isupper() for c in password) and any(c.islower() for c in password):
        rating += 1
    if any(c.isdigit() for c in password):
        rating += 1
    if any(c in string.punctuation for c in password):
        rating += 1
    if len(password) >= 12:
        rating += 1
    if rating == 0:
        return 'weak'
    elif rating < 4:
        return 'medium'
    else:
        return 'strong'

if __name__ == '__main__':
    length = int(input("Enter desired password length: "))
    include_digits = input("Include digits? (y/n): ").lower() == 'y'
    include_punctuation = input("Include punctuation? (y/n): ").lower() == 'y'
    password = generate_password(length, include_digits, include_punctuation)
    print(f"Your password is: {password}")
    strength = check_password_strength(password)
    print(f"The strength of your password is {strength}.")
