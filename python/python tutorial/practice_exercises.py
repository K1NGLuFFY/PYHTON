"""
Practice Exercises for Python Beginners
=====================================

Try these exercises to practice what you learned!
"""

# Exercise 1: Variables
# Create three variables: your name, age, and favorite hobby
# Then print them in a sentence

# TODO: Write your code here
your_name = "Your Name Here"
your_age = 20  # Change this to your age
your_hobby = "coding"  # Change this to your hobby

print(f"Hi, I'm {your_name}. I'm {your_age} years old and I love {your_hobby}!")

# Exercise 2: Simple Calculator
# Create a program that adds two numbers entered by the user

# TODO: Uncomment and complete the code below
# num1 = float(input("Enter first number: "))
# num2 = float(input("Enter second number: "))
# sum_result = num1 + num2
# print(f"The sum is: {sum_result}")

# Exercise 3: Temperature Converter
# Convert Celsius to Fahrenheit
# Formula: F = C × 9/5 + 32

def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit"""
    fahrenheit = celsius * 9/5 + 32
    return fahrenheit

# Test the function
temp_c = 25
temp_f = celsius_to_fahrenheit(temp_c)
print(f"{temp_c}°C = {temp_f}°F")

# Exercise 4: Working with Lists
# Create a shopping list and add/remove items

shopping_list = ["milk", "bread", "eggs"]
print("Original list:", shopping_list)

# Add an item
shopping_list.append("cheese")
print("After adding cheese:", shopping_list)

# Remove an item
shopping_list.remove("bread")
print("After removing bread:", shopping_list)

# Exercise 5: Simple Game - Number Guessing
import random

def number_guessing_game():
    """Simple number guessing game"""
    secret_number = random.randint(1, 10)
    guess = int(input("Guess a number between 1 and 10: "))
    
    if guess == secret_number:
        print("🎉 Congratulations! You guessed it!")
    elif guess < secret_number:
        print("Too low! The number was", secret_number)
    else:
        print("Too high! The number was", secret_number)

# Uncomment to play:
# number_guessing_game()

# Exercise 6: String Manipulation
# Create a simple text formatter

def text_formatter(text):
    """Format text in different ways"""
    print("Original:", text)
    print("Uppercase:", text.upper())
    print("Lowercase:", text.lower())
    print("Title case:", text.title())
    print("Length:", len(text))

text_formatter("hello python world")

# Exercise 7: Simple Loop Practice
# Print numbers 1 to 5 and their squares

print("\nNumbers and their squares:")
for number in range(1, 6):
    square = number ** 2
    print(f"{number} squared = {square}")

# Exercise 8: Dictionary Practice
# Create a simple contact book

contact = {
    "name": "Alice Smith",
    "phone": "123-456-7890",
    "email": "alice@example.com"
}

print("\nContact Information:")
print(f"Name: {contact['name']}")
print(f"Phone: {contact['phone']}")
print(f"Email: {contact['email']}")

# Exercise 9: Function Practice
# Create a function that returns the larger of two numbers

def find_larger(a, b):
    """Return the larger of two numbers"""
    if a > b:
        return a
    else:
        return b

# Test the function
print("\nLarger number between 10 and 20:", find_larger(10, 20))

# Exercise 10: Simple While Loop
# Countdown from 5 to 1

print("\nCountdown:")
count = 5
while count > 0:
    print(count)
    count -= 1
print("Blast off! 🚀")

print("\n✅ Great job practicing! Try modifying these exercises to make them your own.")
