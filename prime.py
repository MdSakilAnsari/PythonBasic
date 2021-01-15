flag=1
i=2
n=int(input("Enter number : "))
if(n>1):
    for i in range(2,n):
        if(n%i==0):
            flag=0
            break
    if(flag==1):
        print("number is prime")
    else:
        print("number is not prime")
else:
    print("Invalid number")    
