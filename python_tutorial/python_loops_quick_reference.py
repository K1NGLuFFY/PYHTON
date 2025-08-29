#!/usr/bin/env python3
"""
Python Loops Quick Reference Card
=================================

Essential patterns and one-liners for everyday use.
"""

print("=== PYTHON LOOPS QUICK REFERENCE ===\n")

# 1. FOR LOOP ESSENTIALS
print("1. FOR LOOP ESSENTIALS")
print("-" * 30)

# Basic patterns
print("Count 0 to 4:")
for i in range(5):
    print(i, end=" ")
print()

print("Count 1 to 5:")
for i in range(1, 6):
    print(i, end=" ")
print()

print("Count by 2s:")
for i in range(0, 10, 2):
    print(i, end=" ")
print()

# List iteration
print("List iteration:")
items = ["a", "b", "c"]
for item in items:
    print(item)

# 2. WHILE LOOP ESSENTIALS
print("\n2. WHILE LOOP ESSENTIALS")
print("-" * 30)

# Basic counter
count = 0
while count < 3:
    print(count)
    count += 1

# 3. LIST COMPREHENSIONS
print("\n3. LIST COMPREHENSIONS")
print("-" * 30)

numbers = [1, 2, 3, 4, 5]

# Squares
squares = [x**2 for x in numbers]
print(f"Squares: {squares}")

# Filter
evens = [x for x in numbers if x % 2 == 0]
print(f"Evens: {evens}")

# 4. COMMON PATTERNS
print("\n4. COMMON PATTERNS")
print("-" * 30)

# Sum
total = sum(numbers)
print(f"Sum: {total}")

# Max
maximum = max(numbers)
print(f"Max: {maximum}")

# 5. CONTROL FLOW
print("\n5. CONTROL FLOW")
print("-" * 30)

# break, continue, else
for i in range(5):
    if i == 3:
        break
    print(i)
else:
    print("Completed")

print("\n=== REFERENCE COMPLETE ===")
