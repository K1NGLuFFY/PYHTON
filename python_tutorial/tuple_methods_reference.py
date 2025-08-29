"""
Python Tuple Methods Reference

This script demonstrates common methods available for Python tuples with examples.
"""

# Creating a sample tuple
fruits = ('apple', 'banana', 'cherry', 'date', 'banana')

print("Original tuple:", fruits)

# count() - Returns the number of times a specified value appears in the tuple
count_banana = fruits.count('banana')
print("Count of 'banana':", count_banana)

# index() - Returns the index of the first item with the specified value
index_cherry = fruits.index('cherry')
print("Index of 'cherry':", index_cherry)

# Note: Tuples are immutable, so methods that modify the tuple like append(), remove(), etc. are not available.

# Demonstrating tuple immutability
try:
    fruits[1] = 'blueberry'
except TypeError as e:
    print("Error when trying to modify tuple:", e)

# Tuples support slicing and concatenation
sliced = fruits[1:4]
print("Sliced tuple (1:4):", sliced)

concatenated = fruits + ('elderberry', 'fig')
print("Concatenated tuple:", concatenated)

# Tuple unpacking example
a, b, c, d, e = fruits
print("Unpacked values:", a, b, c, d, e)
