num1 = 0
num2 = 0

def add():
    sum_result = num1 + num2
    print(f"This is the sum of the two numbers: {sum_result}")

def sub():
    difference = num1 - num2
    print(f"This is the difference of the two numbers: {difference}")

def div():
    if num2 == 0:
        print("Division by zero is undefined.")
    else:
        quotient = num1 / num2
        print(f"This is the quotient of the two numbers: {quotient}")

def mult():
    product = num1 * num2
    print(f"This is the product of the two numbers: {product}")
