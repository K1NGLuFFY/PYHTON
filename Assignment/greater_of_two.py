#!/usr/bin/env python3
"""
Assignment 4: Greater of Two Numbers
This program takes two numbers from the user and outputs the greater number.
"""

def get_greater_number(num1, num2):
    """Return the greater of two numbers."""
    return num1 if num1 > num2 else num2

def main():
    print("=== Greater of Two Numbers ===")
    print("This program will find the greater of two numbers you enter.")
    print()
    
    try:
        # Get first number from user
        num1 = float(input("Enter the first number: "))
        
        # Get second number from user
        num2 = float(input("Enter the second number: "))
        
        # Find the greater number
        greater = get_greater_number(num1, num2)
        
        # Display the result
        print()
        if num1 == num2:
            print(f"Both numbers are equal: {greater}")
        else:
            print(f"The greater number is: {greater}")
            
    except ValueError:
        print("Error: Please enter valid numbers only.")
    except KeyboardInterrupt:
        print("\nProgram interrupted by user.")

if __name__ == "__main__":
    main()
