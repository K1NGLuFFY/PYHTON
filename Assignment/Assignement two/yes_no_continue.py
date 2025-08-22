"""
Yes/No Continuation Program
===========================

A simple program that asks the user if they want to continue.
The program keeps running until the user enters 'n' to stop.
Accepts 'y' or 'n' (case-insensitive) as valid inputs.
"""

print("=== YES/NO CONTINUATION PROGRAM ===")
print("This program will keep asking if you want to continue.")
print("Enter 'y' to continue or 'n' to stop the program.\n")

# Counter to track how many times the user continued
continue_count = 0

# Main program loop
while True:
    # Get user input
    user_input = input("Do you want to continue? (y/n): ").strip().lower()
    
    # Check if user wants to continue
    if user_input == 'y':
        continue_count += 1
        print(f" Continuing... (Continued {continue_count} times)")
        print()  # Empty line for better readability
        
    # Check if user wants to stop
    elif user_input == 'n':
        print(f"\n Stopping the program...")
        break
        
    # Handle invalid input
    else:
        print(" Please enter only 'y' or 'n'!")
        print("   'y' = yes, continue")
        print("   'n' = no, stop the program")
        print()  # Empty line for better readability

print(f"\n=== PROGRAM COMPLETED ===")
print(f"Total times continued: {continue_count}")
print("Thank you for using the program!")
