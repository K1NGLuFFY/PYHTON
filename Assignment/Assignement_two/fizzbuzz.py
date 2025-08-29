"""
FizzBuzz Program
===============

This program prints numbers from 1 to 30 with the following rules:
- For numbers divisible by 3: print "fizz"
- For numbers divisible by 5: print "buzz"
- For numbers divisible by both 3 and 5: print "fizzbuzz"
- For other numbers: print the number itself
"""

print("=== FIZZBUZZ GAME ===")
print("Numbers 1 to 30 with FizzBuzz rules:\n")

# Loop through numbers 1 to 30
for number in range(1, 31):
    if number % 3 == 0 and number % 5 == 0:
        print("fizzbuzz")
    elif number % 3 == 0:
        print("fizz")
    elif number % 5 == 0:
        print("buzz")
    else:
        print(number)

print("\n=== FIZZBUZZ COMPLETE ===")
