import random
import string

def generate_password(length):
    """Generate a random password of specified length"""
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for i in range(length))

if __name__ == '__main__':
    length = int(input("Enter password length: "))
    password = generate_password(length)
    print("Your password is:", password)
