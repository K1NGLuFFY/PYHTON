"""
Positive Numbers Collector
==========================

A simple program that collects integer inputs from the user
and only stops running when the user enters a negative number.
"""

print("=== POSITIVE NUMBERS COLLECTOR ===")
print("Enter positive numbers (or zero) to continue.")
print("Enter a negative number to stop the program.\n")

# Counter to keep track of how many numbers were entered
number_count = 0

# Main program loop
while True:
    try:
        # Get user input
        user_input = input("Enter a number: ")
        
        # Convert to integer
        number = int(user_input)
        
        # Check if number is negative
        if number < 0:
            print(f"\nNegative number ({number}) detected!")
            print("Program stopping...")
            break
        
        # If number is positive or zero, continue
        number_count += 1
        print(f" Number {number} accepted! (Total numbers: {number_count})")
        
    except ValueError:
        print(" Please enter a valid integer number!")

print(f"\n=== PROGRAM COMPLETED ===")
print(f"Total positive numbers/zero entered: {number_count}")
print("Thank you for using the program!")
