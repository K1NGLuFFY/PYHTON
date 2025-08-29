"""
Python Comprehensive Guide: Beyond the Basics
==========================================

This guide covers intermediate Python concepts, best practices, and real-world applications.
Perfect for those who know Python basics and want to level up their skills.
"""

# =============================================================================
# SECTION 1: ADVANCED DATA STRUCTURES & COLLECTIONS
# =============================================================================

from collections import defaultdict, Counter, namedtuple, deque
from typing import List, Dict, Set, Optional, Union, Any
import heapq
import itertools

# Advanced List Operations
def advanced_list_techniques():
    """Demonstrate advanced list operations and comprehensions"""
    
    # List comprehensions with conditions
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    squares = [x**2 for x in numbers if x % 2 == 0]
    print("Even squares:", squares)
    
    # Nested comprehensions
    matrix = [[i*j for j in range(3)] for i in range(3)]
    print("3x3 multiplication table:", matrix)
    
    # Enumerate and zip
    names = ['Alice', 'Bob', 'Charlie']
    scores = [95, 87, 92]
    for index, (name, score) in enumerate(zip(names, scores)):
        print(f"{index+1}. {name}: {score}")

# Working with collections module
def collections_examples():
    """Showcase powerful collections from collections module"""
    
    # defaultdict - automatic default values
    word_count = defaultdict(int)
    text = "hello world hello python world"
    for word in text.split():
        word_count[word] += 1
    print("Word count:", dict(word_count))
    
    # Counter - frequency counting
    colors = ['red', 'blue', 'red', 'green', 'blue', 'red']
    color_counter = Counter(colors)
    print("Most common color:", color_counter.most_common(1))
    
    # namedtuple - readable data structures
    Point = namedtuple('Point', ['x', 'y'])
    p1 = Point(10, 20)
    print(f"Point coordinates: ({p1.x}, {p1.y})")
    
    # deque - efficient double-ended operations
    queue = deque(['task1', 'task2', 'task3'])
    queue.append('task4')      # Add to right
    queue.appendleft('task0')  # Add to left
    print("Queue:", list(queue))

# =============================================================================
# SECTION 2: ADVANCED STRING MANIPULATION
# =============================================================================

import re
from string import Template

def advanced_string_operations():
    """Advanced string formatting and manipulation techniques"""
    
    # f-strings with expressions
    name = "Python"
    version = 3.9
    print(f"Welcome to {name} {version:.1f}!")
    
    # String formatting options
    number = 1234.5678
    print(f"Number: {number:.2f}")      # 1234.57
    print(f"Number: {number:,.2f}")    # 1,234.57
    print(f"Number: {number:>10.2f}")  # Right-aligned
    
    # Advanced string methods
    text = "  Python Programming  "
    print("Original:", repr(text))
    print("Stripped:", repr(text.strip()))
    print("Split:", text.split())
    print("Joined:", "-".join(["Python", "is", "awesome"]))
    
    # Regular expressions
    email_pattern = r'\b[\w.-]+@[\w.-]+\.\w+\b'
    text = "Contact us at support@example.com or sales@company.org"
    emails = re.findall(email_pattern, text)
    print("Found emails:", emails)
    
    # Template strings for safe substitution
    template = Template("Hello $name, your balance is $$${balance}")
    message = template.substitute(name="Alice", balance="1000")
    print(message)

# =============================================================================
# SECTION 3: FILE HANDLING & I/O OPERATIONS
# =============================================================================

import json
import csv
import os
from pathlib import Path

def file_handling_examples():
    """Comprehensive file handling with error management"""
    
    # Working with pathlib (modern approach)
    current_dir = Path.cwd()
    file_path = current_dir / "data" / "example.txt"
    
    # Ensure directory exists
    file_path.parent.mkdir(exist_ok=True)
    
    # Writing to file with context manager
    try:
        with open(file_path, 'w') as f:
            f.write("Hello, Python File Handling!\n")
            f.write("This is line 2\n")
    except IOError as e:
        print(f"Error writing file: {e}")
    
    # Reading file line by line
    try:
        with open(file_path, 'r') as f:
            lines = [line.strip() for line in f]
        print("File contents:", lines)
    except FileNotFoundError:
        print("File not found")
    
    # Working with JSON
    data = {
        "users": [
            {"name": "Alice", "age": 30, "skills": ["Python", "Data Science"]},
            {"name": "Bob", "age": 25, "skills": ["JavaScript", "React"]}
        ]
    }
    
    json_file = file_path.parent / "data.json"
    with open(json_file, 'w') as f:
        json.dump(data, f, indent=2)
    
    # Reading JSON back
    with open(json_file, 'r') as f:
        loaded_data = json.load(f)
    print("Loaded JSON:", loaded_data["users"][0]["name"])
    
    # Working with CSV
    csv_file = file_path.parent / "users.csv"
    with open(csv_file, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['name', 'age', 'department'])
        writer.writeheader()
        writer.writerows([
            {'name': 'Alice', 'age': 30, 'department': 'Engineering'},
            {'name': 'Bob', 'age': 25, 'department': 'Marketing'}
        ])

# =============================================================================
# SECTION 4: ERROR HANDLING & DEBUGGING
# =============================================================================

def comprehensive_error_handling():
    """Advanced error handling patterns and debugging techniques"""
    
    # Custom exception classes
    class ValidationError(Exception):
        """Custom exception for data validation"""
        pass
    
    class DataProcessingError(Exception):
        """Custom exception for data processing"""
        pass
    
    # Comprehensive error handling
    def process_user_data(user_data: Dict[str, Any]) -> Dict[str, Any]:
        """Process user data with robust error handling"""
        try:
            # Validate required fields
            if 'email' not in user_data:
                raise ValidationError("Email is required")
            
            if not isinstance(user_data.get('age'), int):
                raise ValidationError("Age must be an integer")
            
            # Simulate processing
            processed = {
                'email': user_data['email'].lower(),
                'age_group': 'adult' if user_data['age'] >= 18 else 'minor',
                'processed_at': '2024-01-01'
            }
            
            return processed
            
        except ValidationError as e:
            print(f"Validation error: {e}")
            return {'error': str(e)}
<thinking>
I have reviewed the python_basics_tutorial.py and python_cheat_sheet.py files. Both cover fundamental Python concepts such as variables, data types, control flow, functions, lists, dictionaries, and basic operations.

The user wants to go beyond a basic cheat sheet. To do this, I should create a more advanced Python tutorial that covers intermediate topics such as:
- File handling
- Exception handling
- Modules and packages
- List comprehensions
- Generators
- Decorators
- Classes and OOP concepts
- Useful standard libraries
- Possibly some practical examples or mini projects

Next, I will brainstorm a comprehensive plan for this intermediate Python tutorial.
</thinking>

<brainstorm_plan>
<task>Develop a comprehensive intermediate Python tutorial that goes beyond the basics and cheat sheet.</task>
<plan>
1. Introduction: Brief recap of basics and purpose of intermediate tutorial.
2. File Handling: Reading, writing files, working with file paths.
3. Exception Handling: try-except blocks, custom exceptions.
4. Modules and Packages: Importing, creating modules, using pip packages.
5. Data Structures: List comprehensions, sets, tuples, dictionaries advanced usage.
6. Generators and Iterators: Creating and using generators, yield keyword.
7. Decorators: Function decorators, practical examples.
8. Classes and OOP: Classes, objects, inheritance, polymorphism, encapsulation.
9. Useful Standard Libraries: os, sys, datetime, collections, math, random.
10. Practical Examples: Small projects or scripts demonstrating concepts.
11. Summary and Next Steps: Resources for advanced learning.
