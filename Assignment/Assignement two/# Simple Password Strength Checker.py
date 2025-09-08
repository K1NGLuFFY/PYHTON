"""
A simple password checker which checks if a password is strong 
"""

while True:
    password = input("Enter a password: ")

    has_upper = False
    has_lower = False
    has_digit = False

    if len(password) >= 8:
        for char in password:
            if char.isupper():
                has_upper = True
            elif char.islower():
                has_lower = True
            elif char.isdigit():
                has_digit = True

        if has_upper and has_lower and has_digit:
            print("Password is strong!")
            break
        else:
            print("Password must contain uppercase, lowercase, and numbers.")
    else:
        print("Password must be at least 8 characters long.")