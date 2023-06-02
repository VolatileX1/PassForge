import random
import string

def generate_password(length):
    """Generate a random password of specified length"""
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password, 'weak' if len(password) < 8 else 'medium' if len(password) < 12 else 'strong'

if __name__ == '__main__':
    length = int(input("Enter password length: "))
    password, strength = generate_password(length)
    print(f"Your {strength} password is:", password)
