import functionmodule

def checkOp(op):
    if op.lower() == "add":
        functionmodule.add()
    elif op.lower() == "sub":
        functionmodule.sub()
    elif op.lower() == "div":
        functionmodule.div()
    elif op.lower() == "mult":
        functionmodule.mult()
    else:
        print("invalid operation")
