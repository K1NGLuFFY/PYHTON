#!/usr/bin/env python3
"""
Simple Odd or Even Game
Asks the user for a number and determines if it's odd or even
"""

def odd_or_even_game():
    """Main game function"""
    print("Welcome to the Odd or Even Game!")
    print("-" * 30)
    
    while True:
        try:
            # Ask user for input
            user_input = input("\nEnter a number (or 'quit' to exit): ").strip()
            
            # Check if user wants to quit
            if user_input.lower() == 'quit':
                print("Thanks for playing! Goodbye!")
                break
            
            # Convert to integer
            number = int(user_input)
            
            # Check if odd or even
            if number % 2 == 0:
                print(f"{number} is EVEN! 🎲")
            else:
                print(f"{number} is ODD! 🎲")
                
        except ValueError:
            print("Please enter a valid number!")
        except KeyboardInterrupt:
            print("\n\nGame interrupted. Goodbye!")
            break

if __name__ == "__main__":
    odd_or_even_game()
