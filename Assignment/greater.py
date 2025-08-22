"""
Greater of Two Numbers
Finds the greater of two numbers

"""
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if num1 == num2:
    print("the numbers are the same")
elif num1 < num2:
    print(f"num2: {num2} is greater the number")
else:
    print(f"num1: {num1} is greater the number")