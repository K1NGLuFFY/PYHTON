#!/usr/bin/env python3
"""
Python Loops Practice Exercises
==============================

10 hands-on exercises to master Python loops - with solutions!
"""

print("=== PYTHON LOOPS EXERCISES ===\n")

# Exercise 1: Basic Counting
print("EXERCISE 1: Basic Counting")
print("-" * 30)
print("Write a loop to print numbers from 1 to 10")
print("Solution:")
for i in range(1, 11):
    print(i, end=" ")
print("\n")

# Exercise 2: Sum of Numbers
print("\nEXERCISE 2: Sum of Numbers")
print("-" * 30)
print("Calculate the sum of numbers from 1 to 100")
print("Solution:")
total = 0
for i in range(1, 101):
    total += i
print(f"Sum 1-100: {total}")
print(f"Verification: {sum(range(1, 101))}")

# Exercise 3: Even Numbers
print("\nEXERCISE 3: Even Numbers")
print("-" * 30)
print("Print all even numbers from 2 to 20")
print("Solution:")
evens = [x for x in range(2, 21, 2)]
print(f"Even numbers: {evens}")

# Exercise 4: Multiplication Table
print("\nEXERCISE 4: Multiplication Table")
print("-" * 30)
print("Print 5x5 multiplication table")
print("Solution:")
for i in range(1, 6):
    for j in range(1, 6):
        print(f"{i*j:2d}", end=" ")
    print()

# Exercise 5: Factorial
print("\nEXERCISE 5: Factorial")
print("-" * 30)
print("Calculate factorial of 5")
print("Solution:")
def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result
print(f"5! = {factorial(5)}")

# Exercise 6: Prime Numbers
print("\nEXERCISE 6: Prime Numbers")
print("-" * 30)
print("Find all prime numbers up to 20")
print("Solution:")
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

primes = [x for x in range(2, 21) if is_prime(x)]
print(f"Primes up to 20: {primes}")

# Exercise 7: String Reversal
print("\nEXERCISE 7: String Reversal")
print("-" * 30)
print("Reverse the string 'Python'")
print("Solution:")
text = "Python"
reversed_text = ""
for char in text:
    reversed_text = char + reversed_text
print(f"Reversed: {reversed_text}")

# Exercise 8: List Filtering
print("\nEXERCISE 8: List Filtering")
print("-" * 30)
print("Filter numbers greater than 10 from [5, 12, 8, 15, 3, 20]")
print("Solution:")
numbers = [5, 12, 8, 15, 3, 20]
filtered = [x for x in numbers if x > 10]
print(f"Numbers > 10: {filtered}")

# Exercise 9: Pattern Printing
print("\nEXERCISE 9: Pattern Printing")
print("-" * 30)
print("Print right triangle pattern")
print("Solution:")
for i in range(1, 6):
    print("*" * i)

# Exercise 10: Number Guessing Game
print("\nEXERCISE 10: Number Guessing Game")
print("-" * 30)
print("Simple number guessing game with while loop")
print("Solution:")
import random

def guessing_game():
    secret = random.randint(1, 10)
    attempts = 0
    
    while True:
        guess = int(input("Guess 1-10: "))
        attempts += 1
        
        if guess == secret:
            print(f"Correct! {attempts} attempts")
            break
        elif guess < secret:
            print("Too low!")
        else:
            print("Too high!")

# Uncomment to play:
# guessing_game()

print("\n=== EXERCISES COMPLETE ===")
print("Practice these patterns to master loops!")
