"""
This program performs basic arithmetic operations using two variables.
Operations performed:
1. Addition
2. Subtraction
3. Multiplication
4. Division

When run, it displays the results with descriptive text like:
"This is the sum of the two numbers: Sum"
"""

# Two variables
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Ask user which operation they want to perform
operation = input("Which arithmetic operation would you like to perform? (+, -, *, /): ")

# Perform the selected operation based on user choice
if operation == "+":
    # Addition
    sum = num1 + num2
    print(f"This is the sum of the two numbers: {sum}")
elif operation == "-":
    # Subtraction
    Subtraction = num1 - num2
    print(f"This is the difference of the two numbers: {Subtraction}")
elif operation == "*":
    # Multiplication
    Multiplication = num1 * num2
    print(f"This is the product of the two numbers: {Multiplication}")
elif operation == "/":
    # Division
    if num2 != 0:  # Check for division by zero
        Division = num1 / num2
        print(f"This is the quotient of the two numbers: {Division}")
    else:
        print("Error: Cannot divide by zero!")
else:
    print("Invalid operation selected. Please choose from +, -, *, or /.")
