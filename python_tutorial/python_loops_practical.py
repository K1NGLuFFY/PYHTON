#!/usr/bin/env python3
"""
Python Loops - Practical Examples Based on Your Current Files
============================================================

This file demonstrates Python loops using patterns similar to your existing code.
"""

print("=== PYTHON LOOPS - PRACTICAL EXAMPLES ===\n")

# Example 1: Enhanced Odd/Even Game with Loops
print("1. ENHANCED ODD/EVEN GAME WITH LOOPS")
print("-" * 50)

def enhanced_odd_or_even():
    """Enhanced version using different loop types"""
    
    # Using for loop with range
    print("Testing numbers 1-10 with for loop:")
    for num in range(1, 11):
        if num % 2 == 0:
            print(f"{num} is even")
        else:
            print(f"{num} is odd")
    
    print()
    
    # Using while loop for user input
    print("Interactive version with while loop:")
    count = 0
    while count < 3:
        try:
            num = int(input(f"Enter number {count+1}: "))
            if num % 2 == 0:
                print(f"{num} is even")
            else:
                print(f"{num} is odd")
            count += 1
        except ValueError:
            print("Please enter a valid number!")

# Uncomment to run:
# enhanced_odd_or_even()

# Example 2: Find Greater of Multiple Numbers
print("\n2. FIND GREATER OF MULTIPLE NUMBERS")
print("-" * 50)

def find_greatest_of_list():
    """Find the greatest number in a list using loops"""
    
    numbers = [15, 42, 8, 23, 67, 34, 91, 12]
    print(f"Numbers: {numbers}")
    
    # Using for loop to find maximum
    greatest = numbers[0]
    for num in numbers[1:]:
        if num > greatest:
            greatest = num
    
    print(f"Greatest number: {greatest}")
    
    # Alternative using built-in max() with loop
    max_value = max(numbers)
    print(f"Using max(): {max_value}")

find_greatest_of_list()

# Example 3: Number Comparison with Loops
print("\n3. NUMBER COMPARISON WITH LOOPS")
print("-" * 50)

def compare_numbers_loop():
    """Compare multiple pairs of numbers"""
    
    pairs = [(10, 20), (45, 30), (15, 15), (8, 8)]
    
    for num1, num2 in pairs:
        if num1 == num2:
            print(f"{num1} and {num2} are equal")
        elif num1 > num2:
            print(f"{num1} is greater than {num2}")
        else:
            print(f"{num2} is greater than {num1}")

compare_numbers_loop()

# Example 4: Input Validation with Loops
print("\n4. INPUT VALIDATION WITH LOOPS")
print("-" * 50)

def get_valid_number():
    """Keep asking for input until valid number is provided"""
    
    while True:
        try:
            num = int(input("Enter a positive number: "))
            if num > 0:
                return num
            else:
                print("Please enter a positive number!")
        except ValueError:
            print("That's not a valid number!")

# Uncomment to test:
# valid_num = get_valid_number()
# print(f"You entered: {valid_num}")

# Example 5: Menu System with Loops
print("\n5. MENU SYSTEM WITH LOOPS")
print("-" * 50)

def number_operations_menu():
    """Simple menu system using loops"""
    
    while True:
        print("\nNumber Operations Menu:")
        print("1. Check if number is odd/even")
        print("2. Find greater of two numbers")
        print("3. Exit")
        
        choice = input("Enter your choice (1-3): ")
        
        if choice == '1':
            try:
                num = int(input("Enter a number: "))
                if num % 2 == 0:
                    print(f"{num} is even")
                else:
                    print(f"{num} is odd")
            except ValueError:
                print("Invalid input!")
                
        elif choice == '2':
            try:
                num1 = int(input("Enter first number: "))
                num2 = int(input("Enter second number: "))
                
                if num1 == num2:
                    print("Numbers are equal")
                elif num1 > num2:
                    print(f"{num1} is greater")
                else:
                    print(f"{num2} is greater")
            except ValueError:
                print("Invalid input!")
                
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")

# Uncomment to run:
# number_operations_menu()

# Example 6: Advanced Loop Patterns
print("\n6. ADVANCED LOOP PATTERNS")
print("-" * 50)

# Nested loops for patterns
def print_number_pattern():
    """Print a number pattern using nested loops"""
    
    print("Number pattern:")
    for i in range(1, 6):
        for j in range(1, i+1):
            print(j, end=" ")
        print()

print_number_pattern()

# Loop with break and continue
def find_first_even(numbers):
    """Find first even number in a list"""
    for num in numbers:
        if num % 2 == 0:
            return num
    return None

test_numbers = [3, 7, 11, 14, 18, 21]
first_even = find_first_even(test_numbers)
print(f"First even in {test_numbers}: {first_even}")

# Example 7: Loop with else clause
print("\n7. LOOP WITH ELSE CLAUSE")
print("-" * 50)

def check_prime(n):
    """Check if a number is prime using loop with else"""
    if n < 2:
        return False
    
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            print(f"{n} is not prime (divisible by {i})")
            break
    else:
        print(f"{n} is prime!")

check_prime(17)
check_prime(15)

# Example 8: List processing with loops
print("\n8. LIST PROCESSING WITH LOOPS")
print("-" * 50)

def process_numbers():
    """Process a list of numbers using various loop techniques"""
    
    numbers = [12, 7, 5, 64, 14, 9, 83, 15]
    
    # Find all odd numbers
    odd_numbers = [num for num in numbers if num % 2 != 0]
    print(f"Original numbers: {numbers}")
    print(f"Odd numbers: {odd_numbers}")
    
    # Find numbers greater than 10
    greater_than_10 = [num for num in numbers if num > 10]
    print(f"Numbers > 10: {greater_than_10}")
    
    # Calculate squares
    squares = [num**2 for num in numbers]
    print(f"Squares: {squares}")

process_numbers()

print("\n=== PRACTICAL LOOPS COMPLETE ===")
print("These examples show how loops work with:")
print("- User input validation")
print("- Number comparisons")
print("- List processing")
print("- Menu systems")
print("- Pattern generation")
