from modulefun import show
from modulefun import add
from modulefun import sub
from modulefun import febo
from modulefun import mul
from modulefun import factorial
print("Enten your choice\n===============")
print("Press 1 for addition")
print("Press 2 for substion")
print("Press 3 for multiplication")
print("Press 4 for factorial")
print("Press 5 for febonacci series")
print("===================")
n=int(input("Enter choice "))

if(n==1):
    a=int(input("Enter Value 1 "))
    b=int(input("Enter Value 2 "))
    sum=add(a,b)
    print(sum)
elif(n==2):
    a=int(input("Enter Value 1 "))
    b=int(input("Enter Value 2 "))
    dif=sub(a,b)
    print(dif)
elif(n==3):
    a=int(input("Enter Value 1 "))
    b=int(input("Enter Value 2 "))
    pro=mul(a,b)
    print(pro)
if(n==4):
    v=int(input("Enter value to find factorial "))
    f=factorial(v)
    print("facrorial is =",f)
if(n==5):
    febo()
else:
    exit()