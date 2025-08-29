"""
Python Quick Reference Guide
============================

Keep this handy while learning Python!
"""

# VARIABLES
name = "text"        # String
age = 25            # Integer
price = 19.99       # Float
is_valid = True     # Boolean

# BASIC OPERATIONS
# Math: + - * / // % **
# Comparison: == != < > <= >=
# Logic: and or not

# STRINGS
text = "Hello World"
text.upper()        # HELLO WORLD
text.lower()        # hello world
text.title()        # Hello World
len(text)           # 11
text[0]            # 'H' (first character)

# LISTS
my_list = [1, 2, 3]
my_list.append(4)   # [1, 2, 3, 4]
my_list[0]          # 1 (first item)
len(my_list)        # 3

# DICTIONARIES
person = {"name": "John", "age": 30}
person["name"]      # "John"
person["age"]       # 30

# IF STATEMENTS
if age > 18:
    print("Adult")
elif age > 12:
    print("Teen")
else:
    print("Child")

# LOOPS
# For loop
for i in range(5):
    print(i)  # 0, 1, 2, 3, 4

# While loop
count = 0
while count < 3:
    print(count)
    count += 1

# FUNCTIONS
def greet(name):
    """Say hello to someone"""
    return f"Hello, {name}!"

# USEFUL FUNCTIONS
print("Hello")          # Display output
input("Enter: ")        # Get user input
int("123")              # Convert to integer
float("3.14")           # Convert to float
str(123)                # Convert to string
len("hello")            # Get length
type(123)               # Check data type

# COMMON ERRORS TO AVOID
# - Forgetting colons (:) after if/for/def
# - Using wrong indentation
# - Mixing spaces and tabs
# - Forgetting parentheses in print()
# - Using = instead of == for comparison

# TIPS FOR BEGINNERS
# 1. Start with simple programs
# 2. Read error messages carefully
# 3. Practice regularly
# 4. Don't be afraid to experiment
# 5. Use print() to debug your code
