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

# while True:
#     # Two variables
#     num1 = int(input("Enter the first number: "))
#     num2 = int(input("Enter the second number: "))

#     # Ask user which operation they want to perform
#     operation = input("Which arithmetic operation would you like to perform? (+, -, *, /): ")

#     def addition():
#         sum_result = num1 + num2
#         print(f"This is the sum of the two numbers: {sum_result}")

#     def subtraction():
#         difference = num1 - num2
#         print(f"This is the difference of the two numbers: {difference}")

#     def division():
#         if num2 == 0:
#             print("Division by zero is undefined.")
#         else:
#             quotient = num1 / num2
#             print(f"This is the quotient of the two numbers: {quotient}")

#     def multiplication():
#         product = num1 * num2
#         print(f"This is the product of the two numbers: {product}")

#     # Perform the selected operation based on user choice
#     if operation == "+":
#         addition()
#     elif operation == "-":
#         subtraction()
#     elif operation == "/":
#         division()
#     elif operation == "*":
#         multiplication()
#     else:
#         print("Invalid operation selected.")

#     # Ask if the user wants to continue
#     continue_choice = input("Do you want to perform another operation? (Y/n): ").strip().lower()
#     if continue_choice == 'n':
#         break


choice 

"""
main.py
inputmodule- get all the  input - num1 num2 op
functions module - add division sub mult functions
logic module - if



while:
    inputmodule.getnum1
    inputmodule.getnum2
    inputmodule.getop

    logicModule.checkOp(op)
    
----------------------------------------

inputmodule
def getnum1():
def getnum2():
def getop():
---------------------------------------

function module 
def add
def sub
def div
def mult

-----------------------------------------

logicmodule
if op.lower == "add":
    functionmodule.add()
elif op.lower == "sub":
    functionmodule.sub()
elif op.lower == "div":
    functionmodule.div()
elif op.lower == "mult":
    functionmodule.mult()
else:
    print("invalid operation")
"""