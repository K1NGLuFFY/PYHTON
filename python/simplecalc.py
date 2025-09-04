"""
simple calculator, that gets two user int input and op returns 
sum, diff, qoutient, product

"""
#user input num1 and num2 
num1 = int(input("input your first number: "))
num2 = int(input("input your second number:"))

#operation input 
op = input("enter your operation: ")

#sum, difference, quotient, product
sum = num1 + num2
difference = num1 - num2
quotient = num1 / num2
product = num1 * num2

# conditional statement
if (op.lower() == "sum"):
    print(f"this is the sum of the two numbers: {sum}")
elif (op.lower() == "difference"):
    print(f"this is the difference of the two numbers: {difference}")
elif (op.lower() == "quotient"):
    print(f"this is the quotient of the two numbers: {quotient}")
    if (num2 == 0):
        print("undefined")
    else(op.lower() == "product"):
    print(f"this is the product of the two numbers: {product}")




