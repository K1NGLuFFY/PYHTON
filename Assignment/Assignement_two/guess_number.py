"""
Guess the Number Game
=====================

A simple number guessing game where the user tries to guess a secret number.
The game continues until the user guesses correctly.
"""

import random

print("=== GUESS THE NUMBER GAME ===")
print("Try to guess the secret number between 1 and 10!\n")

# Set the secret number randomly between 1 and 10
secret_number = random.randint(1, 10)

# Initialize guess counter
attempts = 0

# Game loop
while True:
    try:
        # Get user's guess
        guess = int(input("Enter your guess: "))
        attempts += 1
        
        # Check if guess is correct
        if guess == secret_number:
            print(f" Correct! You win!")
            print(f"It took you {attempts} attempt(s) to guess the number.")
            break
        else:
            print(" Wrong guess! Try again.\n")
            
    except ValueError:
        print("  Please enter a valid number!\n")

print("\n=== GAME OVER ===")
