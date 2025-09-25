import inputmodule
import logicmodule
import functionmodule

while True:
    functionmodule.num1 = inputmodule.getnum1()
    functionmodule.num2 = inputmodule.getnum2()
    op = inputmodule.getop()
    
    logicmodule.checkOp(op)
    
    continue_choice = input("Do you want to perform another operation? (Y/n): ").strip().lower()
    if continue_choice == 'n':
        break
