"""
Age Verification Program
=======================

A simple program that verifies if the user is an adult (18+ years old).
The program keeps running until the user enters an age that is above 18.
"""

print("=== AGE VERIFICATION ===")
print("Please enter your age to verify you are an adult (18+ years old).")
print("The program will continue until you enter a valid age above 18.\n")

# Main program loop
while True:
    try:
        # Get user input
        age_input = input("Enter your age: ")
        
        # Convert to integer
        age = int(age_input)
        
        # Check if age is valid (positive number)
        if age < 0:
            print("  Age cannot be negative! Please enter a valid age.\n")
        # Check if age is 18 or above
        elif age >= 18:
            print(f" Verification successful! You are {age} years old.")
            print("Access granted. Welcome, adult user!")
            break
        else:
            print(f" Access denied! You are only {age} years old.")
            print("You must be 18 or older to continue.\n")
    except ValueError:
        print("  Please enter a valid number for your age!\n")

print("\n=== PROGRAM COMPLETED ===")
print("Thank you for using the age verification system!")
