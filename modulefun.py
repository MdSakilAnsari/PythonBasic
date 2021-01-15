pi=3.14
def show():
    print("Hello Sakil")
def add(a,b):
    return a+b
def sub(a,b):
    return a-b

def mul(a,b):
    return a*b
def factorial(x):
    fact=x
    for i in range(2,x):
        fact=fact*i
    return fact
def febo():
    a=0
    b=1
    print(a,end=",")
    print(b,end=",")  
    for i in range(3,10):
        c=a+b
        print(c,end=",")
        (a,b)=(b,c)
    
