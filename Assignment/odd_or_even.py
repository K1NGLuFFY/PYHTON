#!/usr/bin/env python3
"""
Simple Odd or Even Game
Asks the user for a number and determines if it's odd or even
"""

def odd_or_even_game():
    print("Odd or Even Game")
    print("-----------------")
    while True:
        user_input = input("Enter a number (or 'quit' to exit): ")
        if user_input == 'quit':
            print("Goodbye!")
            break
        number = int(user_input)
        if number % 2 == 0:
            print(number, "is EVEN!")
        else:
            print(number, "is ODD!")

if __name__ == "__main__":
    odd_or_even_game()
