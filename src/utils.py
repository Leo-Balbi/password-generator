import random
import string

def generate_password(length=12, complexity='medium'):
    chars = ''
    if complexity == 'low':
        chars = string.ascii_lowercase
    elif complexity == 'medium':
        chars = string.ascii_letters + string.digits
    elif complexity == 'high':
        chars = string.ascii_letters + string.digits + string.punctuation

    return ''.join(random.choice(chars) for _ in range(length))

def save_password(password):
    with open("src/data/passwords.txt", "a") as file:
        file.write(password + "\n")