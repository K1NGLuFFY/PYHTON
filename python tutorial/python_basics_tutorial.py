"""
Python Basics Tutorial for Complete Beginners
============================================

Welcome to your first Python lesson! This tutorial will teach you the fundamentals
of Python programming step by step.

What is Python?
---------------
Python is a programming language that's:
- Easy to read and write (like English)
- Used everywhere (websites, data science, AI, automation)
- Free and open source
- Great for beginners!

Let's start with the basics...
"""

# 1. Your First Python Program
print("Hello, World!")  # This displays text on screen

# 2. Variables - Storing Information
# Think of variables as labeled boxes that store data

name = "Alice"          # Text (string)
age = 25               # Whole number (integer)
height = 5.6           # Decimal number (float)
is_student = True      # True/False (boolean)

print("My name is:", name)
print("I am", age, "years old")

# 3. Basic Data Types
"""
Python has several built-in data types:

- int: Whole numbers (1, 2, 100, -50)
- float: Decimal numbers (3.14, 2.5, -0.5)
- str: Text ("hello", 'Python', "123")
- bool: True or False
"""

# 4. Working with Numbers
a = 10
b = 3

print("Addition:", a + b)        # 13
print("Subtraction:", a - b)     # 7
print("Multiplication:", a * b)  # 30
print("Division:", a / b)        # 3.333...
print("Floor Division:", a // b) # 3
print("Modulus:", a % b)         # 1 (remainder)
print("Power:", a ** b)          # 1000

# 5. Working with Text (Strings)
first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name  # String concatenation
print("Full name:", full_name)

# String methods
message = "hello python"
print(message.upper())      # HELLO PYTHON
print(message.title())      # Hello Python
print(len(message))         # 12 (length)

# 6. Getting User Input
# Uncomment the lines below to try it:
# user_name = input("What's your name? ")
# print("Nice to meet you,", user_name)

# 7. Making Decisions (if statements)
temperature = 75

if temperature > 80:
    print("It's hot outside!")
elif temperature > 60:
    print("Nice weather!")
else:
    print("It's cold!")

# 8. Loops - Repeating Actions
# For loop - when you know how many times
print("Counting to 5:")
for i in range(1, 6):
    print(i)

# While loop - when you don't know how many times
count = 0
while count < 3:
    print("Count is:", count)
    count += 1  # Same as count = count + 1

# 9. Lists - Collections of Items
fruits = ["apple", "banana", "cherry"]
print("First fruit:", fruits[0])      # apple
print("All fruits:", fruits)
fruits.append("orange")               # Add item
print("Updated fruits:", fruits)

# 10. Dictionaries - Key-Value Pairs
person = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}
print(person["name"], "lives in", person["city"])

# 11. Functions - Reusable Code Blocks
def greet_user(username):
    """This function greets a user"""
    return f"Hello, {username}! Welcome to Python."

# Using the function
print(greet_user("Bob"))
print(greet_user("Charlie"))

# 12. Simple Calculator Function
def add_numbers(x, y):
    """Add two numbers and return the result"""
    return x + y

result = add_numbers(5, 3)
print("5 + 3 =", result)

"""
Practice Exercises:
1. Create variables for your favorite color, number, and food
2. Write a program that asks for user's name and age, then prints a greeting
3. Create a list of 3 movies you like and print each one
4. Write a function that multiplies two numbers
5. Use an if statement to check if a number is positive, negative, or zero

Remember:
- Python is case-sensitive (Name and name are different)
- Use # for comments
- Indentation matters in Python (use 4 spaces)
- Don't be afraid to experiment and make mistakes!
"""

print("\n🎉 Congratulations! You've learned Python basics!")
