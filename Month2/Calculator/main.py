import inputmodule
import logicmodule
import functionmodule as fm

while True:
    fm.num1 = inputmodule.getnum1()
    fm.num2 = inputmodule.getnum2()
    op = inputmodule.getop()
    
    logicmodule.checkOp(op)
    
    continue_choice = input("Do you want to perform another operation? (Y/n): ").strip().lower()
    if continue_choice == 'n' or continue_choice == 'no':
        break
