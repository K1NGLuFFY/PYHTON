import functionmodule as fm

def checkOp(op):
    if op.lower() == "add":
        fm.add()
    elif op.lower() == "sub":
        fm.sub()
    elif op.lower() == "div":
        fm.div()
    elif op.lower() == "mult":
        fm.mult()
    else:
        print("invalid operation")
