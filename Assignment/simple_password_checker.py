# Simple Password Checker
# Checks if password is "MR FRANK"

def check_password():
    """Check if the entered password matches 'MR FRANK'"""
    password = input("Enter password: ")
    
    if password == "MR FRANK":
        print("Access granted")
    else:
        print("Access denied")

# Run the program
if __name__ == "__main__":
    check_password()
