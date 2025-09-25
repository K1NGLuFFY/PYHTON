def getnum1():
    while True:
        try:
            num1 = int(input("Enter the first number: "))
            return num1
        except ValueError:
            print("Please enter a valid number.")

def getnum2():
    while True:
        try:
            num2 = int(input("Enter the second number: "))
            return num2
        except ValueError:
            print("Please enter a valid number.")

def getop():
    operation = input("Which arithmetic operation would you like to perform? (add, sub, mult, div): ")
    return operation
