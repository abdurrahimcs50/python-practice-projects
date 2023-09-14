'''
Problem 2: Password Strength Checker

Your task is to create a password strength checker for a new user registration system. Write a Python program that takes a password as input and checks its strength based on the following rules:

The password must be at least 8 characters long.
The password must contain at least one uppercase letter.
The password must contain at least one lowercase letter.
The password must contain at least one digit (0-9).
The password must contain at least one special character (e.g., !, @, #, $, %, etc.).
Write a program that checks the strength of a password and prints whether it's strong or weak.

'''

# Password Strength Checker
def check_password_strength(password):
    # Check if the password is at least 8 characters long
    if len(password) < 8:
        return "Weak: Password must be at least 8 characters long."

    # Check if the password contains at least one uppercase letter
    if not any(char.isupper() for char in password):
        return "Weak: Password must contain at least one uppercase letter."

    # Check if the password contains at least one lowercase letter
    if not any(char.islower() for char in password):
        return "Weak: Password must contain at least one lowercase letter."

    # Check if the password contains at least one digit
    if not any(char.isdigit() for char in password):
        return "Weak: Password must contain at least one digit."

    # Check if the password contains at least one special character
    special_characters = "!@#$%^&*()_+{}[]|\/:;<>,.?~-"
    if not any(char in special_characters for char in password):
        return "Weak: Password must contain at least one special character."

    # If all checks pass, the password is strong
    return "Strong: Password meets all criteria."

# Input: Get the password from the user
password = input("Enter your password: ")
result = check_password_strength(password)
print(result)
