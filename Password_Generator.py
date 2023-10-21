import random
import string

def generate_password(length):
    # Defining the characters that will be in used for the password
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation

    # Combining the characters into a single string
    all_characters = lowercase_letters + uppercase_letters + digits + special_characters

    # Generating  a random password of the required length
    password = ''.join(random.choices(all_characters, k=length))

    return password

#Getting input from the useer for the length and number of passwords to be generated
password_length = int(input("Enter the length of the password: "))
num_passwords = int(input("Enter the number of passwords to generate: "))

# Generating the specified number of passwords and printing them
for i in range(num_passwords):
    password = generate_password(password_length)
    print(password)