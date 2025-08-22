"""
================================================================================
PYTHON COMPLETE CHEAT SHEET - BEGINNER TO ADVANCED
================================================================================

This comprehensive guide covers Python from absolute basics to advanced concepts.
Use it as a quick reference or learning roadmap.

CONTENTS:
1. Python Basics
2. Data Types & Structures
3. Control Flow
4. Functions & Lambdas
5. Object-Oriented Programming
6. File Handling
7. Error Handling
8. Modules & Packages
9. Advanced Python Features
10. Popular Libraries & Frameworks
11. Best Practices & Tips
12. Performance Optimization
"""

# ==============================================================================
# 1. PYTHON BASICS
# ==============================================================================

# Variables & Assignment
name = "Python"           # String
version = 3.9            # Float (decimal)
is_awesome = True        # Boolean
nothing = None           # NoneType

# Multiple assignment
x, y, z = 1, 2, 3
a = b = c = 0

# Type checking
type(name)              # <class 'str'>
isinstance(name, str)   # True

# Type conversion
int("123")              # 123
float("3.14")           # 3.14
str(100)                # "100"
bool(1)                 # True
list("hello")           # ['h', 'e', 'l', 'l', 'o']

# ==============================================================================
# 2. DATA TYPES & STRUCTURES
# ==============================================================================

# NUMBERS
# Integers
num1 = 42
num2 = -17

# Floats
pi = 3.14159
scientific = 1.23e-4  # 0.000123

# Complex numbers
complex_num = 3 + 4j

# STRINGS
text = "Hello, Python!"
multiline = """
This is a
multiline string
"""

# String methods
text.upper()            # "HELLO, PYTHON!"
text.lower()            # "hello, python!"
text.title()            # "Hello, Python!"
text.strip()            # Remove whitespace
text.replace("Python", "World")
text.split(",")         # ["Hello", " Python!"]
"-".join(["a", "b", "c"])  # "a-b-c"

# String formatting
name = "Alice"
age = 25
f"Hello, {name}! You are {age} years old."
"Hello, {}! You are {} years old.".format(name, age)
"Hello, %s! You are %d years old." % (name, age)

# String indexing and slicing
text[0]                 # 'H'
text[-1]                # '!'
text[0:5]               # "Hello"
text[::-1]              # Reverse string

# LISTS (ordered, mutable)
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")
fruits.insert(1, "grape")
fruits.remove("banana")
popped = fruits.pop()   # Remove and return last item
fruits.extend(["kiwi", "mango"])
fruits.sort()
fruits.reverse()

# List comprehension
squares = [x**2 for x in range(10)]
even_squares = [x**2 for x in range(10) if x % 2 == 0]

# TUPLES (ordered, immutable)
coordinates = (10, 20)
x, y = coordinates      # Unpacking
single_tuple = (42,)    # Note the comma

# DICTIONARIES (key-value pairs)
person = {
    "name": "John",
    "age": 30,
    "city": "New York"
}
person["email"] = "john@example.com"
person.get("phone", "Not provided")
person.keys()
person.values()
person.items()

# Dictionary comprehension
squares_dict = {x: x**2 for x in range(5)}

# SETS (unique elements, unordered)
unique_numbers = {1, 2, 3, 3, 4}  # {1, 2, 3, 4}
unique_numbers.add(5)
unique_numbers.discard(3)
set1 = {1, 2, 3}
set2 = {3, 4, 5}
set1.union(set2)        # {1, 2, 3, 4, 5}
set1.intersection(set2) # {3}
set1.difference(set2)   # {1, 2}

# ==============================================================================
# 3. CONTROL FLOW
# ==============================================================================

# IF STATEMENTS
age = 18
if age >= 18:
    print("Adult")
elif age >= 13:
    print("Teenager")
else:
    print("Child")

# Ternary operator
status = "Adult" if age >= 18 else "Minor"

# LOOPS
# For loop
for i in range(5):      # 0, 1, 2, 3, 4
    print(i)

for fruit in fruits:
    print(fruit)

for index, value in enumerate(fruits):
    print(f"{index}: {value}")

# While loop
count = 0
while count < 5:
    print(count)
    count += 1

# Loop control
for num in range(10):
    if num == 5:
        break           # Exit loop
    if num % 2 == 0:
        continue        # Skip to next iteration
    print(num)

# ==============================================================================
# 4. FUNCTIONS & LAMBDAS
# ==============================================================================

# Basic function
def greet(name, greeting="Hello"):
    """Return a greeting message."""
    return f"{greeting}, {name}!"

# Function with variable arguments
def add_all(*args):
    """Add all numbers provided."""
    return sum(args)

def build_profile(**kwargs):
    """Build a user profile from keyword arguments."""
    return kwargs

# Lambda functions (anonymous functions)
square = lambda x: x**2
add = lambda x, y: x + y

# Higher-order functions
numbers = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, numbers))
evens = list(filter(lambda x: x % 2 == 0, numbers))
total = sum(numbers)

# Decorators
def timer(func):
    import time
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print(f"{func.__name__} took {time.time() - start:.4f} seconds")
        return result
    return wrapper

@timer
def slow_function():
    import time
    time.sleep(1)
    return "Done!"

# ==============================================================================
# 5. OBJECT-ORIENTED PROGRAMMING
# ==============================================================================

class Animal:
    """Base animal class."""
    species = "Unknown"
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def speak(self):
        return f"{self.name} makes a sound"
    
    @classmethod
    def get_species(cls):
        return cls.species
    
    @staticmethod
    def info():
        return "This is an animal class"

class Dog(Animal):
    """Dog class inherits from Animal."""
    species = "Canine"
    
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed
    
    def speak(self):
        return f"{self.name} barks: Woof!"
    
    @property
    def human_years(self):
        return self.age * 7

# Using classes
dog = Dog("Buddy", 3, "Golden Retriever")
print(dog.speak())
print(f"Human years: {dog.human_years}")

# Magic methods
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    
    def __str__(self):
        return f"Vector({self.x}, {self.y})"
    
    def __len__(self):
        return int((self.x**2 + self.y**2)**0.5)

# ==============================================================================
# 6. FILE HANDLING
# ==============================================================================

# Reading files
with open("file.txt", "r") as file:
    content = file.read()
    lines = file.readlines()

# Writing files
with open("output.txt", "w") as file:
    file.write("Hello, World!")
    file.writelines(["Line 1\n", "Line 2\n"])

# Appending to files
with open("log.txt", "a") as file:
    file.write("New log entry\n")

# Working with CSV
import csv
with open("data.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row["name"], row["age"])

# Working with JSON
import json
data = {"name": "Alice", "age": 30}
with open("data.json", "w") as file:
    json.dump(data, file, indent=2)

with open("data.json", "r") as file:
    loaded_data = json.load(file)

# ==============================================================================
# 7. ERROR HANDLING
# ==============================================================================

# Basic try-except
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")
except Exception as e:
    print(f"An error occurred: {e}")
else:
    print("Division successful!")
finally:
    print("This always runs")

# Raising exceptions
def validate_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    return age

# Custom exceptions
class CustomError(Exception):
    """Custom exception class."""
    pass

# ==============================================================================
# 8. MODULES & PACKAGES
# ==============================================================================

# Importing modules
import math
from datetime import datetime, timedelta
import os.path as path
from collections import defaultdict, Counter

# Creating modules
# Save as my_module.py
def useful_function():
    return "This is useful!"

# Using the module
# import my_module
# print(my_module.useful_function())

# Package structure
"""
my_package/
    __init__.py
    module1.py
    module2.py
    subpackage/
        __init__.py
        module3.py
"""

# ==============================================================================
# 9. ADVANCED PYTHON FEATURES
# ==============================================================================

# Generators
def fibonacci(n):
    """Generate Fibonacci numbers up to n."""
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

# Using generators
for num in fibonacci(10):
    print(num)

# Generator expression
squares_gen = (x**2 for x in range(10))

# Context managers
class ManagedFile:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
    
    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()

with ManagedFile("hello.txt", "w") as f:
    f.write("Hello, Context Manager!")

# Regular expressions
import re
pattern = r"\b\w+\b"
text = "Hello world! Python is great."
matches = re.findall(pattern, text)

# Itertools
from itertools import count, cycle, chain, combinations, permutations

# Infinite counter
for i in count(10):
    if i > 15:
        break
    print(i)

# Functional programming tools
from functools import reduce, lru_cache

@lru_cache(maxsize=128)
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)

# ==============================================================================
# 10. POPULAR LIBRARIES & FRAMEWORKS
# ==============================================================================

# NUMPY (Numerical computing)
import numpy as np
arr = np.array([1, 2, 3, 4, 5])
mean = np.mean(arr)
std = np.std(arr)

# PANDAS (Data manipulation)
import pandas as pd
df = pd.DataFrame({
    'name': ['Alice', 'Bob', 'Charlie'],
    'age': [25, 30, 35]
})
filtered = df[df['age'] > 25]

# MATPLOTLIB (Plotting)
import matplotlib.pyplot as plt
plt.plot([1, 2, 3, 4], [1, 4, 9, 16])
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Simple Plot')
plt.show()

# REQUESTS (HTTP requests)
import requests
response = requests.get('https://api.github.com')
data = response.json()

# FLASK (Web framework)
from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({'message': 'Hello, World!'})

# SQLALCHEMY (Database ORM)
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)

# ==============================================================================
# 11. BEST PRACTICES & TIPS
# ==============================================================================

# PEP 8 Style Guide
"""
- Use 4 spaces for indentation
- Limit lines to 79 characters
- Use lowercase with underscores for variables
- Use CapWords for classes
- Use UPPERCASE for constants
"""

# Docstrings
def example_function(param1, param2):
    """
    Brief description of the function.
    
    Args:
        param1: Description of param1
        param2: Description of param2
    
    Returns:
        Description of return value
    
    Raises:
        ValueError: When invalid input provided
    """
    pass

# Type hints
from typing import List, Dict, Optional, Union

def process_data(items: List[str]) -> Dict[str, int]:
    result: Dict[str, int] = {}
    for item in items:
        result[item] = len(item)
    return result

# Virtual environments
"""
python -m venv myenv
source myenv/bin/activate  # Linux/Mac
myenv\Scripts\activate     # Windows
pip install package_name
"""

# Testing with pytest
"""
def test_addition():
    assert add(2, 3) == 5
    
Run: pytest test_file.py
"""

# Logging
import logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# ==============================================================================
# 12. PERFORMANCE OPTIMIZATION
# ==============================================================================

# List vs Generator
# Bad: Creates entire list in memory
squares_list = [x**2 for x in range(1000000)]

# Good: Generates values on demand
squares_gen = (x**2 for x in range(1000000))

# Using built-in functions
# Bad
result = []
for item in items:
    result.append(len(item))

# Good
result = list(map(len, items))

# Profiling
import cProfile
import pstats

def slow_function():
    return sum(i**2 for i in range(10000))

cProfile.run('slow_function()', 'output.stats')
p = pstats.Stats('output.stats')
p.sort_stats('cumulative').print_stats(10)

# Memory management
import sys
sys.getsizeof([])      # Size of empty list
sys.getsizeof([1, 2, 3])  # Size of list with items

# ==============================================================================
# QUICK REFERENCE COMMANDS
# ==============================================================================

# Python shell
"""
python                    # Start interactive shell
python -i script.py       # Run script and enter interactive mode
python -c "print('Hello')" # Execute code directly
"""

# Package management
"""
pip install package_name
pip install -r requirements.txt
pip freeze > requirements.txt
pip list
pip show package_name
"""

# Debugging
"""
import pdb
pdb.set_trace()          # Set breakpoint
python -m pdb script.py  # Debug script
"""

# ==============================================================================
# COMMON PITFALLS TO AVOID
# ==============================================================================

# Mutable default arguments
# Bad
def bad_function(items=[]):
    items.append(1)
    return items

# Good
def good_function(items=None):
    if items is None:
        items = []
    items.append(1)
    return items

# Variable scope
# Global variables
global_var = 10

def modify_global():
    global global_var
    global_var += 1

# Late binding closures
# Bad
functions = [lambda: i for i in range(3)]  # All return 2

# Good
functions = [lambda x=i: x for i in range(3)]  # Returns 0, 1, 2

# ==============================================================================
# USEFUL ONE-LINERS
# ==============================================================================

# Swap variables
a, b = b, a

# Flatten list of lists
flat = [item for sublist in nested_list for item in sublist]

# Remove duplicates while preserving order
unique = list(dict.fromkeys(my_list))

# Check if all elements are true
all_true = all(my_list)

# Check if any element is true
any_true = any(my_list)

# Find most common element
from collections import Counter
most_common = Counter(my_list).most_common(1)[0][0]

# ==============================================================================
# LEARNING RESOURCES
# ==============================================================================

# Official documentation: https://docs.python.org/3/
# Interactive tutorials: https://www.learnpython.org/
# Practice problems: https://leetcode.com/, https://www.hackerrank.com/domains/tutorials/10-days-of-python
# Books: "Python Crash Course", "Automate the Boring Stuff with Python"
# YouTube channels: Corey Schafer, Tech With Tim, Sentdex

print("Python Cheat Sheet loaded successfully!")
