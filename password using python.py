import random
import string

def generate_password(length, use_numbers=True, use_symbols=True):
    # Define character sets
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    numbers = string.digits
    symbols = string.punctuation
    
    # Build the pool of characters to choose from
    char_pool = lowercase + uppercase
    if use_numbers:
        char_pool += numbers
    if use_symbols:
        char_pool += symbols

    # Ensure the password includes at least one character from each required set
    password = []
    if use_numbers:
        password.append(random.choice(numbers))
    if use_symbols:
        password.append(random.choice(symbols))
    password.append(random.choice(lowercase))
    password.append(random.choice(uppercase))

    # Fill the rest of the password length with random choices from the pool
    while len(password) < length:
        password.append(random.choice(char_pool))

    # Shuffle the resulting password list and convert it to a string
    random.shuffle(password)
    return ''.join(password)

# User input for password requirements
length = int(input("Enter the desired password length: "))
use_numbers = input("Include numbers? (yes/no): ").strip().lower() == 'yes'
use_symbols = input("Include symbols? (yes/no): ").strip().lower() == 'yes'

# Generate and display the password
password = generate_password(length, use_numbers, use_symbols)
print("Generated password:", password)
