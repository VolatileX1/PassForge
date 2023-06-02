import random
import string

def generate_password(length=12, include_digits=True, include_punctuation=True):
    """Generate a random password with customizable options"""
    characters = string.ascii_letters + (string.digits if include_digits else '') + \
                 (string.punctuation if include_punctuation else '')
    password = ''.join(random.choice(characters) for i in range(length))
    rating = sum([1 for check in [lambda s: len(s) >= 8,
                                  lambda s: any(c.isupper() for c in s) and any(c.islower() for c in s),
                                  lambda s: any(c.isdigit() for c in s),
                                  lambda s: any(c in string.punctuation for c in s),
                                  lambda s: len(s) >= 12] if check(password)])
    return password, 'weak' if rating < 3 else 'medium' if rating < 5 else 'strong'

if __name__ == '__main__':
    length = int(input("Enter desired password length: "))
    include_digits = input("Include digits? (y/n): ").lower() == 'y'
    include_punctuation = input("Include punctuation? (y/n): ").lower() == 'y'
    website = input("Enter website: ")
    email = input("Enter email ID: ")
    username = input("Enter username: ")
    password, strength = generate_password(length, include_digits, include_punctuation)
    
    # Save password along with associated website, email ID and username to a file
    with open('passwords.txt', 'a') as f:
        f.write(f"Website: {website}\nEmail ID: {email}\nUsername: {username}\nPassword: {password}\n\n")
        
    print(f"Your {strength} password for {website} is: {password}")
