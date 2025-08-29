"""
Python List Methods Reference

This script demonstrates common methods available for Python lists with examples.
"""

# Creating a sample list
fruits = ['apple', 'banana', 'cherry', 'date']

print("Original list:", fruits)

# append() - Adds an element to the end of the list
fruits.append('elderberry')
print("After append('elderberry'):", fruits)

# extend() - Extends list by appending elements from another iterable
fruits.extend(['fig', 'grape'])
print("After extend(['fig', 'grape']):", fruits)

# insert() - Inserts an element at a specified position
fruits.insert(2, 'blueberry')
print("After insert(2, 'blueberry'):", fruits)

# remove() - Removes the first item with the specified value
fruits.remove('banana')
print("After remove('banana'):", fruits)

# pop() - Removes and returns item at the given index (default last)
popped_item = fruits.pop()
print("After pop():", fruits)
print("Popped item:", popped_item)

# clear() - Removes all items from the list
temp_list = fruits.copy()
temp_list.clear()
print("After clear():", temp_list)

# index() - Returns the index of the first item with the specified value
index_cherry = fruits.index('cherry')
print("Index of 'cherry':", index_cherry)

# count() - Returns the number of times a specified value appears in the list
count_apple = fruits.count('apple')
print("Count of 'apple':", count_apple)

# sort() - Sorts the list in ascending order
fruits.sort()
print("After sort():", fruits)

# reverse() - Reverses the order of the list
fruits.reverse()
print("After reverse():", fruits)

# copy() - Returns a shallow copy of the list
fruits_copy = fruits.copy()
print("Copy of the list:", fruits_copy)
