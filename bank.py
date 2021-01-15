from bankmodule import cbal
from bankmodule import wth
from bankmodule import dep
while True:
    print("Enten your choice\n===============")
    print("Press 1 to check Balance ")
    print("Press 2 to deposit amount ")
    print("Press 3 to withdraw amount ")
    print("Press 4 to exit ")
    print("===================")
    n=int(input("Enter choice "))
    if(n==1):
        cbal()
    elif(n==2):
        a=int(input("Enter amount to be deposit "))
        bal=dep(a)
        print("After deposit available amount = ",bal)
    elif(n==3):
        w=int(input("Enter amount to be withdraw "))
        bal=wth(w)
        print("After withdraw available amount = ",bal)
    if(n==4):
        exit()
    