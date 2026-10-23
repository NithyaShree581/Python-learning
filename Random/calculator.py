def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mult(a,b):
    return a*b
def div(a,b):
    try:
        return a/b
    except: 
        raise ZeroDivisionError("The value of b can't be zero")
