"""
COMPREHENSIVE GUIDE TO PYTHON STRING METHODS AND IMPORTS
========================================================

This guide covers all essential Python string methods and how to import
various modules for string manipulation and processing.
"""

# ==============================================================================
# 1. BASIC STRING CREATION AND IMPORT STATEMENTS
# ==============================================================================

# Basic string creation
single_quotes = 'Hello World'
double_quotes = "Hello World"
triple_quotes = """This is a
multiline string"""
raw_string = r"C:\Users\Name\Documents"  # Raw string (no escape processing)

# Import statements for string operations
import string  # Built-in string module
import re      # Regular expressions
import os      # Operating system interface
import sys     # System-specific parameters
from datetime import datetime  # Date/time operations

# ==============================================================================
# 2. ESSENTIAL STRING METHODS
# ==============================================================================

text = "  Hello Python World!  "
sample = "python is awesome"

# Case conversion methods
print("Case conversion:")
print(f"upper(): {text.upper()}")          # "  HELLO PYTHON WORLD!  "
print(f"lower(): {text.lower()}")          # "  hello python world!  "
print(f"title(): {sample.title()}")        # "Python Is Awesome"
print(f"capitalize(): {sample.capitalize()}") # "Python is awesome"
print(f"swapcase(): {'Hello'.swapcase()}") # "hELLO"

# Whitespace and character manipulation
print("\nWhitespace and character manipulation:")
print(f"strip(): '{text.strip()}'")        # "Hello Python World!"
print(f"lstrip(): '{text.lstrip()}'")      # "Hello Python World!  "
print(f"rstrip(): '{text.rstrip()}'")      # "  Hello Python World!"
print(f"replace(): {text.replace('Python', 'Java')}") # "  Hello Java World!  "

# Searching and finding
print("\nSearching and finding:")
print(f"find('Python'): {text.find('Python')}")    # 7
print(f"rfind('o'): {text.rfind('o')}")            # 15
print(f"index('Python'): {text.index('Python')}")  # 7
print(f"rindex('o'): {text.rindex('o')}")          # 15
print(f"count('o'): {text.count('o')}")            # 2

# Boolean checks
print("\nBoolean checks:")
print(f"startswith('Hello'): {text.startswith('Hello')}")  # False (due to spaces)
print(f"endswith('!'): {text.endswith('!')}")              # False (due to spaces)
print(f"isalpha(): {'abc'.isalpha()}")                     # True
print(f"isdigit(): {'123'.isdigit()}")                     # True
print(f"isalnum(): {'abc123'.isalnum()}")                  # True
print(f"isspace(): {'   '.isspace()}")                     # True
print(f"islower(): {'hello'.islower()}")                   # True
print(f"isupper(): {'HELLO'.isupper()}")                   # True

# Splitting and joining
print("\nSplitting and joining:")
words = text.strip().split()
print(f"split(): {words}")                    # ['Hello', 'Python', 'World!']
print(f"split('o'): {text.split('o')}")       # ['  Hell', ' Pyth', 'n W', 'rld!  ']
print(f"rsplit('o'): {text.rsplit('o')}")     # ['  Hell', ' Pyth', 'n W', 'rld!  ']
print(f"join(): {'-'.join(words)}")           # "Hello-Python-World!"

# Padding and alignment
print("\nPadding and alignment:")
print(f"center(20): '{'hello'.center(20)}'")      # "       hello        "
print(f"ljust(15): '{'hello'.ljust(15)}'")        # "hello          "
print(f"rjust(15): '{'hello'.rjust(15)}'")        # "          hello"
print(f"zfill(8): {'42'.zfill(8)}")               # "00000042"

# Encoding and formatting
print("\nEncoding and formatting:")
print(f"encode(): {'hello'.encode('utf-8')}")     # b'hello'
print(f"format(): {'Hello {}'.format('World')}")  # "Hello World"

# ==============================================================================
# 3. STRING MODULE UTILITIES
# ==============================================================================

print("\nString module utilities:")
print(f"string.ascii_letters: {string.ascii_letters}")
print(f"string.ascii_lowercase: {string.ascii_lowercase}")
print(f"string.ascii_uppercase: {string.ascii_uppercase}")
print(f"string.digits: {string.digits}")
print(f"string.hexdigits: {string.hexdigits}")
print(f"string.octdigits: {string.octdigits}")
print(f"string.punctuation: {string.punctuation}")
print(f"string.whitespace: {repr(string.whitespace)}")

# Generate random strings using string module
import random
random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
print(f"Random string: {random_string}")

# ==============================================================================
# 4. REGULAR EXPRESSIONS (re MODULE)
# ==============================================================================

print("\nRegular expressions:")
text = "Email me at john@example.com or jane@test.org"

# Find all email addresses
emails = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', text)
print(f"Emails found: {emails}")

# Search for pattern
match = re.search(r'@(\w+)\.', text)
if match:
    print(f"Domain: {match.group(1)}")

# Replace patterns
clean_text = re.sub(r'@\w+\.', '@company.', text)
print(f"Cleaned text: {clean_text}")

# ==============================================================================
# 5. F-STRINGS (MODERN STRING FORMATTING)
# ==============================================================================

print("\nF-strings (modern formatting):")
name = "Alice"
age = 30
height = 5.8

# Basic f-string
print(f"Name: {name}, Age: {age}")

# Expressions in f-strings
print(f"Next year: {age + 1}")
print(f"Height in cm: {height * 30.48:.1f}")

# Formatting options
print(f"Percentage: {0.7567:.2%}")      # 75.67%
print(f"Hex: {255:#x}")                 # 0xff
print(f"Binary: {42:b}")                # 101010
print(f"Padded: {7:05d}")               # 00007

# ==============================================================================
# 6. COMMON IMPORT PATTERNS FOR STRING PROCESSING
# ==============================================================================

# Standard library imports for text processing
import csv           # CSV file handling
import json          # JSON serialization
import html          # HTML escaping
import urllib.parse  # URL encoding/decoding
import base64        # Base64 encoding
import hashlib       # Hash functions
import unicodedata   # Unicode database

# Example: URL encoding
url = "https://example.com/search?q=python tutorial"
encoded = urllib.parse.quote(url)
decoded = urllib.parse.unquote(encoded)
print(f"URL encoded: {encoded}")
print(f"URL decoded: {decoded}")

# Example: Base64 encoding
message = "Hello World"
encoded_b64 = base64.b64encode(message.encode()).decode()
decoded_b64 = base64.b64decode(encoded_b64).decode()
print(f"Base64 encoded: {encoded_b64}")
print(f"Base64 decoded: {decoded_b64}")

# ==============================================================================
# 7. ADVANCED STRING OPERATIONS
# ==============================================================================

# String translation (character mapping)
translation_table = str.maketrans('aeiou', '12345')
text = "hello world"
translated = text.translate(translation_table)
print(f"Translated: {translated}")  # h2ll4 w4rld

# Partition and splitlines
text = "first:second:third"
print(f"partition(': '): {text.partition(':')}")  # ('first', ':', 'second:third')
print(f"rpartition(': '): {text.rpartition(':')}") # ('first:second', ':', 'third')

multiline = "Line 1\nLine 2\r\nLine 3"
print(f"splitlines(): {multiline.splitlines()}")  # ['Line 1', 'Line 2', 'Line 3']

# String interpolation (old style)
name = "Bob"
print("Hello %s!" % name)              # Hello Bob!
print("Value: %d, Price: $%.2f" % (42, 19.99))

# ==============================================================================
# 8. PRACTICAL EXAMPLES AND USE CASES
# ==============================================================================

# 1. User input validation
def validate_username(username):
    """Validate username: 3-20 chars, alphanumeric and underscores only"""
    if 3 <= len(username) <= 20 and username.replace('_', '').isalnum():
        return True
    return False

# 2. Password strength checker
def check_password_strength(password):
    """Check password strength"""
    if len(password) < 8:
        return "Weak: Too short"
    if not any(c.isupper() for c in password):
        return "Weak: No uppercase letters"
    if not any(c.isdigit() for c in password):
        return "Weak: No numbers"
    return "Strong password"

# 3. Text processing pipeline
def process_text(text):
    """Clean and process text"""
    # Remove extra whitespace
    text = ' '.join(text.split())
    # Convert to lowercase
    text = text.lower()
    # Remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))
    return text

# 4. Generate secure tokens
def generate_secure_token(length=32):
    """Generate cryptographically secure random token"""
    import secrets
    return secrets.token_urlsafe(length)

# ==============================================================================
# 9. BEST PRACTICES AND PERFORMANCE TIPS
# ==============================================================================

"""
STRING MANIPULATION BEST PRACTICES:

1. Use f-strings for most string formatting (Python 3.6+)
2. Use join() instead of + for concatenating many strings
3. Use raw strings (r"") for regex patterns and file paths
4. Prefer string methods over regex for simple operations
5. Use triple quotes for multiline strings and docstrings
6. Be careful with encoding/decoding - specify encoding explicitly
7. Use string constants from string module for character sets
8. Validate and sanitize user input strings
9. Use format() for complex formatting requirements
10. Consider performance: string operations are generally fast in Python
"""

# Performance comparison: join vs concatenation
import time

def test_join_vs_concat():
    words = ['hello'] * 10000
    
    # Using join (faster)
    start = time.time()
    result_join = ''.join(words)
    time_join = time.time() - start
    
    # Using concatenation (slower)
    start = time.time()
    result_concat = ''
    for word in words:
        result_concat += word
    time_concat = time.time() - start
    
    print(f"Join: {time_join:.6f}s, Concat: {time_concat:.6f}s")
    print(f"Join is {time_concat/time_join:.1f}x faster")

# Uncomment to test performance
# test_join_vs_concat()

# ==============================================================================
# 10. COMMON PITFALLS AND SOLUTIONS
# ==============================================================================

"""
COMMON STRING PITFALLS:

1. Mutable vs Immutable: Strings are immutable - operations return new strings
2. Encoding issues: Always specify encoding when reading/writing files
3. String vs Bytes: Remember the difference (str vs bytes)
4. Locale awareness: Some string operations are locale-dependent
5. Memory usage: Large string operations can be memory-intensive
6. Special characters: Be careful with escape sequences
7. Unicode: Python 3 uses Unicode by default, but be aware of encoding issues
"""

print("\n" + "="*80)
print("STRING METHODS AND IMPORTS GUIDE COMPLETE!")
print("Run this file to see all examples in action.")
print("="*80)
