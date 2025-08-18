"""
Python Intermediate Tutorial
============================

Now that you've mastered Python basics, let's dive deeper into more powerful concepts!
This tutorial covers intermediate Python topics that will make you a more efficient programmer.
"""

# 1. List Comprehensions - Elegant way to create lists
# Instead of:
squares = []
for x in range(10):
    squares.append(x**2)

# Use list comprehension:
squares = [x**2 for x in range(10)]
print("Squares:", squares)

# With conditions
even_squares = [x**2 for x in range(10) if x % 2 == 0]
print("Even squares:", even_squares)

# 2. Dictionary Comprehensions
word_lengths = {word: len(word) for word in ["python", "programming", "awesome"]}
print("Word lengths:", word_lengths)

# 3. Lambda Functions - Anonymous functions
# Regular function
def multiply(x, y):
    return x * y

# Lambda equivalent
multiply_lambda = lambda x, y: x * y

print("Regular:", multiply(3, 4))
print("Lambda:", multiply_lambda(3, 4))

# 4. Map, Filter, Reduce - Functional programming tools
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Map - apply function to all items
doubled = list(map(lambda x: x * 2, numbers))
print("Doubled:", doubled)

# Filter - keep items that match condition
evens = list(filter(lambda x: x % 2 == 0, numbers))
print("Evens:", evens)

# 5. Advanced String Operations
text = "  Python Programming is Fun!  "

# String formatting (f-strings)
name = "Alice"
age = 25
formatted = f"{name} is {age} years old"
print(formatted)

# Advanced string methods
print("Original:", text)
print("Stripped:", text.strip())
print("Lower:", text.lower())
print("Replace:", text.replace("Python", "Java"))
print("Split:", text.split())
print("Join:", "-".join(["Python", "is", "awesome"]))

# 6. Exception Handling - Handling errors gracefully
def divide_numbers(a, b):
    """Safely divide two numbers"""
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        return "Cannot divide by zero!"
    except TypeError:
        return "Please provide numbers only"
    finally:
        print("Division operation completed")

print(divide_numbers(10, 2))
print(divide_numbers(10, 0))
print(divide_numbers("10", 2))

# 7. File Handling - Working with files
# Writing to a file
with open("sample.txt", "w") as file:
    file.write("Hello from Python!\n")
    file.write("This is line 2\n")

# Reading from a file
with open("sample.txt", "r") as file:
    content = file.read()
    print("File content:", content)

# 8. Classes and Objects - Object-Oriented Programming
class Dog:
    """A simple Dog class"""
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def bark(self):
        return f"{self.name} says Woof!"
    
    def get_human_years(self):
        return self.age * 7

# Using the class
my_dog = Dog("Buddy", 3)
print(my_dog.bark())
print(f"{my_dog.name} is {my_dog.get_human_years()} in human years")

# 9. Inheritance - Building on existing classes
class Puppy(Dog):
    """A puppy is a young dog"""
    
    def __init__(self, name):
        super().__init__(name, 0)  # Call parent constructor
    
    def play(self):
        return f"{self.name} is playing with a ball!"

my_puppy = Puppy("Max")
print(my_puppy.play())
print(my_puppy.bark())

# 10. Working with JSON - Data interchange format
import json

# Python dictionary
person = {
    "name": "John Doe",
    "age": 30,
    "skills": ["Python", "JavaScript", "SQL"],
    "address": {
        "street": "123 Main St",
        "city": "Boston"
    }
}

# Convert to JSON string
json_string = json.dumps(person, indent=2)
print("JSON string:")
print(json_string)

# Parse JSON back to Python
parsed = json.loads(json_string)
print("Parsed name:", parsed["name"])

# 11. Working with CSV files
import csv

# Writing CSV
with open("people.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Age", "City"])
    writer.writerow(["Alice", 25, "New York"])
    writer.writerow(["Bob", 30, "Chicago"])

# Reading CSV
with open("people.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print("CSV Row:", row)

# 12. Regular Expressions - Pattern matching
import re

text = "Contact us at support@example.com or sales@company.org"

# Find email addresses
emails = re.findall(r'\b[\w.-]+@[\w.-]+\.\w+\b', text)
print("Found emails:", emails)

# Validate phone number
phone_pattern = r'^\d{3}-\d{3}-\d{4}$'
phone = "123-456-7890"
if re.match(phone_pattern, phone):
    print("Valid phone number")
else:
    print("Invalid phone number")

# 13. Decorators - Modify function behavior
def timer_decorator(func):
    """Decorator to time function execution"""
    import time
    
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start:.4f} seconds")
        return result
    
    return wrapper

@timer_decorator
def slow_function():
    """A function that takes some time"""
    import time
    time.sleep(1)
    return "Done!"

print(slow_function())

# 14. Generators - Memory-efficient iteration
def fibonacci_generator(n):
    """Generate Fibonacci numbers up to n terms"""
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

# Using the generator
fib_numbers = list(fibonacci_generator(10))
print("Fibonacci sequence:", fib_numbers)

# 15. Advanced Collections - collections module
from collections import Counter, defaultdict, namedtuple

# Counter - Count occurrences
words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
word_count = Counter(words)
print("Word counts:", word_count)

# Defaultdict - Dictionary with default values
grouped_words = defaultdict(list)
for word in ["cat", "car", "dog", "door"]:
    grouped_words[word[0]].append(word)
print("Grouped by first letter:", dict(grouped_words))

# Namedtuple - Lightweight objects
Point = namedtuple('Point', ['x', 'y'])
p = Point(10, 20)
print(f"Point at ({p.x}, {p.y})")

# 16. Working with dates and times
from datetime import datetime, timedelta

now = datetime.now()
print("Current time:", now)
print("Formatted:", now.strftime("%Y-%m-%d %H:%M:%S"))

# Date arithmetic
tomorrow = now + timedelta(days=1)
print("Tomorrow:", tomorrow.strftime("%Y-%m-%d"))

# 17. Advanced error handling with custom exceptions
class CustomError(Exception):
    """Custom exception for our application"""
    pass

def validate_age(age):
    if age < 0:
        raise CustomError("Age cannot be negative")
    elif age > 150:
        raise CustomError("Age seems unrealistic")
    return True

try:
    validate_age(-5)
except CustomError as e:
    print("Custom error:", str(e))

# 18. Context Managers - Better resource management
class ManagedFile:
    """Custom context manager for file handling"""
    
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
    
    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()

# Using the context manager
with ManagedFile("test.txt", "w") as f:
    f.write("Using custom context manager!")

print("\n🎉 Congratulations! You've learned intermediate Python concepts!")
print("Practice these concepts by building small projects and solving problems.")
