"""
Comprehensive Guide to All Python Data Types
==========================================

This file contains detailed information about every data type available in Python,
including built-in types, collection types, and advanced types.
"""

# ============================================
# 1. NUMERIC TYPES
# ============================================

# Integer - Whole numbers (positive, negative, zero)
integer_num = 42
negative_int = -100
zero = 0
large_int = 999999999999999999999999999999999999999999999999

# Float - Decimal numbers
float_num = 3.14159
negative_float = -2.71828
scientific_notation = 1.23e-4  # 0.000123
infinity = float('inf')
negative_infinity = float('-inf')
not_a_number = float('nan')

# Complex - Complex numbers with real and imaginary parts-
complex_num = 3 + 4j
complex_from_vars = complex(2, 5)  # 2 + 5j
complex_conjugate = complex_num.conjugate()  # 3 - 4j

# ============================================
# 2. BOOLEAN TYPE
# ============================================

boolean_true = True
boolean_false = False
from_comparison = 5 > 3  # True
from_function = bool(1)  # True (non-zero is True)
from_string = bool("hello")  # True (non-empty string is True)
from_list = bool([])  # False (empty list is False)

# ============================================
# 3. SEQUENCE TYPES
# ============================================

# String - Immutable sequence of Unicode characters
string_single = 'Hello, Python!'
string_double = "Hello, World!"
string_triple = """This is a
multi-line string"""
string_raw = r"C:\Users\name\folder"  # Raw string, no escape sequences
string_formatted = f"Value: {integer_num}"  # f-string formatting
string_unicode = "Hello 世界 🌍"  # Unicode support

# List - Ordered, mutable collection
empty_list = []
numbers_list = [1, 2, 3, 4, 5]
mixed_list = [1, "hello", 3.14, True, [1, 2, 3]]
nested_list = [[1, 2], [3, 4], [5, 6]]
list_comprehension = [x**2 for x in range(5)]  # [0, 1, 4, 9, 16]

# Tuple - Ordered, immutable collection
empty_tuple = ()
single_tuple = (42,)  # Note the comma for single-element tuple
coordinates = (10.0, 20.0)
rgb_color = (255, 128, 0)
nested_tuple = ((1, 2), (3, 4))
tuple_without_parens = 1, 2, 3  # Tuple packing

# Range - Immutable sequence of numbers
range_basic = range(5)  # 0, 1, 2, 3, 4
range_start_stop = range(2, 8)  # 2, 3, 4, 5, 6, 7
range_step = range(1, 10, 2)  # 1, 3, 5, 7, 9

# ============================================
# 4. SET TYPES
# ============================================

# Set - Unordered collection of unique elements
empty_set = set()  # Note: {} creates empty dict, not set
number_set = {1, 2, 3, 4, 5}
mixed_set = {1, "hello", 3.14, True}  # Note: True == 1
set_from_list = set([1, 2, 2, 3, 3, 4])  # {1, 2, 3, 4}

# Frozenset - Immutable version of set
frozen = frozenset([1, 2, 3, 4, 5])
frozen_empty = frozenset()

# ============================================
# 5. MAPPING TYPES
# ============================================

# Dictionary - Key-value pairs
empty_dict = {}
person = {"name": "Alice", "age": 30, "city": "New York"}
mixed_dict = {"numbers": [1, 2, 3], "valid": True, "nested": {"key": "value"}}
dict_from_tuples = dict([("a", 1), ("b", 2), ("c", 3)])
dict_comprehension = {x: x**2 for x in range(5)}  # {0:0, 1:1, 2:4, 3:9, 4:16}

# OrderedDict - Dictionary that remembers insertion order (Python 3.7+)
from collections import OrderedDict
ordered = OrderedDict([('first', 1), ('second', 2), ('third', 3)])

# defaultdict - Dictionary with default values
from collections import defaultdict
word_count = defaultdict(int)
word_count['hello'] += 1  # No KeyError, defaults to 0

# ============================================
# 6. BINARY TYPES
# ============================================

# Bytes - Immutable sequence of bytes
bytes_literal = b'hello'
bytes_from_string = "hello".encode('utf-8')
bytes_from_list = bytes([104, 101, 108, 108, 111])  # b'hello'

# Bytearray - Mutable sequence of bytes
byte_array = bytearray(b'hello')
byte_array[0] = 72  # Change 'h' to 'H' -> b'Hello'

# Memoryview - Memory view object
data = b'hello world'
memory_view = memoryview(data)
slice_view = memory_view[0:5]  # b'hello'

# ============================================
# 7. NONE TYPE
# ============================================

none_value = None
empty_function_result = print("Hello")  # Returns None
default_argument = None  # Common for default parameter values

# ============================================
# 8. ADVANCED TYPES FROM COLLECTIONS MODULE
# ============================================

from collections import namedtuple, deque, Counter, ChainMap

# NamedTuple - Lightweight object type
Point = namedtuple('Point', ['x', 'y'])
p = Point(11, y=22)
print(f"Point: ({p.x}, {p.y})")

# Deque - Double-ended queue
dq = deque([1, 2, 3])
dq.appendleft(0)
dq.append(4)
print("Deque:", list(dq))  # [0, 1, 2, 3, 4]

# Counter - Multiset for counting
counter = Counter(['red', 'blue', 'red', 'green', 'blue', 'red'])
print("Color counts:", counter)  # Counter({'red': 3, 'blue': 2, 'green': 1})

# ChainMap - Multiple dicts as single mapping
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
chain = ChainMap(dict1, dict2)
print("ChainMap:", chain['b'])  # 2 (from dict1)

# ============================================
# 9. CUSTOM CLASSES (USER-DEFINED TYPES)
# ============================================

class Person:
    """A simple Person class"""
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self):
        return f"{self.name} is {self.age} years old"
    
    def have_birthday(self):
        self.age += 1
        return self.age

# Creating instances
person1 = Person("Alice", 30)
person2 = Person("Bob", 25)

# ============================================
# 10. FUNCTION TYPES
# ============================================

# Regular function
def greet(name):
    return f"Hello, {name}!"

# Lambda function
square = lambda x: x**2
add = lambda x, y: x + y

# Generator function
def fibonacci(n):
    """Generate first n Fibonacci numbers"""
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

# ============================================
# 11. TYPE CHECKING AND CONVERSION
# ============================================

# Checking types
print(type(42))  # <class 'int'>
print(isinstance(42, int))  # True
print(isinstance(42, (int, float)))  # True

# Type conversion
int_from_float = int(3.14)  # 3
float_from_int = float(42)  # 42.0
str_from_int = str(42)  # "42"
list_from_string = list("hello")  # ['h', 'e', 'l', 'l', 'o']
tuple_from_list = tuple([1, 2, 3])  # (1, 2, 3)
set_from_list = set([1, 2, 2, 3])  # {1, 2, 3}
dict_from_tuples = dict([('a', 1), ('b', 2)])  # {'a': 1, 'b': 2}

# ============================================
# 12. TYPE HINTING (PYTHON 3.5+)
# ============================================

from typing import List, Dict, Set, Tuple, Optional, Union, Any

# Basic type hints
def process_numbers(numbers: List[int]) -> int:
    return sum(numbers)

# Optional types
def find_user(user_id: int) -> Optional[str]:
    users = {1: "Alice", 2: "Bob"}
    return users.get(user_id)

# Union types
def process_value(value: Union[int, str]) -> str:
    return str(value)

# Complex type hints
def process_data(data: Dict[str, List[Tuple[int, str]]]) -> Set[str]:
    result = set()
    for key, values in data.items():
        for num, text in values:
            result.add(f"{key}_{num}_{text}")
    return result

# ============================================
# 13. SPECIAL TYPES
# ============================================

# Ellipsis - Used in slicing and type hints
ellipsis_type = ...
numpy_slice = [1, 2, 3, 4, 5][...]  # Used in NumPy

# NotImplemented - Returned by binary special methods
result = NotImplemented

# ============================================
# 14. IMMUTABLE VS MUTABLE TYPES
# ============================================

# Immutable types (cannot be changed after creation)
immutable_examples = {
    "int": 42,
    "float": 3.14,
    "complex": 1+2j,
    "bool": True,
    "str": "hello",
    "tuple": (1, 2, 3),
    "frozenset": frozenset([1, 2, 3]),
    "bytes": b"hello"
}

# Mutable types (can be changed after creation)
mutable_examples = {
    "list": [1, 2, 3],
    "dict": {"a": 1, "b": 2},
    "set": {1, 2, 3},
    "bytearray": bytearray(b"hello"),
    "custom_objects": Person("Alice", 30)
}

# ============================================
# 15. PRACTICAL EXAMPLES
# ============================================

def demonstrate_all_types():
    """Demonstrate usage of all Python data types"""
    
    # Create a comprehensive data structure
    user_profile = {
        "user_id": 1001,
        "username": "python_dev",
        "email": "dev@python.org",
        "age": 28,
        "is_active": True,
        "skills": ["Python", "JavaScript", "SQL"],
        "address": {
            "street": "123 Code St",
            "city": "Techville",
            "coordinates": (40.7128, -74.0060)
        },
        "preferences": {"theme": "dark", "notifications": True},
        "scores": [95.5, 87.0, 92.5],
        "metadata": frozenset(["verified", "premium"]),
        "profile_pic": b'\x89PNG\r\n\x1a\n...',  # Binary image data
        "last_login": None
    }
    
    # Process the data
    print("User Profile Summary:")
    print(f"Name: {user_profile['username']}")
    print(f"Skills: {', '.join(user_profile['skills'])}")
    print(f"Average Score: {sum(user_profile['scores'])/len(user_profile['scores']):.1f}")
    print(f"Location: {user_profile['address']['city']}")
    
    # Type checking
    for key, value in user_profile.items():
        print(f"{key}: {type(value).__name__} = {value}")

# ============================================
# 16. SUMMARY TABLE
# ============================================

"""
SUMMARY OF ALL PYTHON DATA TYPES:

1. Numeric Types:
   - int: Whole numbers
   - float: Decimal numbers
   - complex: Complex numbers

2. Boolean Type:
   - bool: True/False

3. Sequence Types:
   - str: Text strings
   - list: Ordered, mutable collections
   - tuple: Ordered, immutable collections
   - range: Sequence of numbers

4. Set Types:
   - set: Unordered unique elements
   - frozenset: Immutable set

5. Mapping Types:
   - dict: Key-value pairs
   - collections.OrderedDict: Ordered dictionary
   - collections.defaultdict: Dictionary with defaults

6. Binary Types:
   - bytes: Immutable byte sequences
   - bytearray: Mutable byte sequences
   - memoryview: Memory view objects

7. None Type:
   - None: Null/undefined value

8. Advanced Types:
   - namedtuple: Lightweight objects
   - deque: Double-ended queue
   - Counter: Counting elements
   - ChainMap: Multiple dictionaries

9. User-Defined Types:
   - Classes and instances
   - Functions and lambdas
   - Generators

10. Special Types:
    - Ellipsis (...)
    - NotImplemented
"""

if __name__ == "__main__":
    print("=== Python Data Types Comprehensive Guide ===")
    demonstrate_all_types()





# primitve data types and non primitive data types
# Primitive Data Types
# 1. Numeric Types: int, float, complex
# 2. Boolean Type: bool
# 3. None Type: NoneType
# Non-Primitive Data Types
# 1. Sequence Types: str, list, tuple, range
# 2. Set Types: set, frozenset
# 3. Mapping Types: dict, collections.OrderedDict, collections.defaultdict
print(a)  # Output: 5
print(b)  # Output: biscuit
print("This is a simple addition:", 3 + 5)  # Output: This is a simple addition: 8
# Simple calculator that adds two numbers
def add_numbers(num1, num2):
    """
    Simple calculator that adds two numbers.
    
    Parameters:
    num1 (int): First number
    num2 (int): Second number
    
    Returns:
    int: Sum of num1 and num2
    """
    return num1 + num2
result = add_numbers(num1, num2)
print("The sum of", num1, "and", num2, "is:", result
)  # Output: The sum of 10 and 3 is: 13
print("This is a simple addition:", 3 + 5)  # Output: This is a simple addition: 8
print("This is a simple addition:", 3 + 5)  # Output: This is a simple addition: 8
print("This is a simple addition:", 3 + 5)  # Output: This
# is a simple addition: 8
print("This is a simple addition:", 3 + 5)  # Output: This is a simple addition: 8
frozenset = frozenset([1, 2, 3, 4, 5])# a frozen set is an immutable version of a set
print("Frozen set:", frozenset)  # Output: Frozen set: frozenset