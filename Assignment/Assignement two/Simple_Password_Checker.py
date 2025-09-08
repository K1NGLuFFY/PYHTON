"""
A simple password checker which checks if a password is strong
It checks for length, uppercase, lowercase, and numeric characters.
A user inputs a password and receives feedback on its strength.
"""

while True:
    try:
        password = input("Enter a password (or type 'exit' to quit): ")
    except (EOFError, KeyboardInterrupt):
        print("\nInput interrupted. Exiting password checker. Goodbye!")
        break

    if password.lower() == 'exit':
        print("Exiting password checker. Goodbye!")
        break

    errors = []

    if len(password) < 8:
        errors.append("Password must be at least 8 characters long.")

    if not any(char.isupper() for char in password):
        errors.append("Password must contain at least one uppercase letter.")

    if not any(char.islower() for char in password):
        errors.append("Password must contain at least one lowercase letter.")

    if not any(char.isdigit() for char in password):
        errors.append("Password must contain at least one number.")

    if not errors:
        print("Password is strong!")
        break
    else:
        print("\nPassword is weak. Please fix the following issues:")
        for error in errors:
            print(f"- {error}")
        print()