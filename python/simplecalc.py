"""
simple calculator, that gets two user int input and op returns 
sum, diff, qoutient, product

"""
#user input num1 and num2 
num1 = int(input("input your first number: "))
num2 = int(input("input your second number:"))

#operation input 
op = input("enter your opertaion: ")

#sum, differene, quotient, product
sum = num1 + num2
difference = num1 - num2
quotient = num1 / num2
product = num1 * num2

# conditional statement
if (op == "sum"):
    print(f"this is the sum of the two numbers: {sum}")
elif (op == "difference"):
    print(f"this is the difference of the two numbers: {difference}")
elif (op == "quotient"):
    print(f"this is the quotient of the two numbers: {quotient}")
else :
    print(f"this is the product of two numbers: {product}")
    
print("end of program")
