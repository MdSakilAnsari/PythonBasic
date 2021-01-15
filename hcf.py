def gcd(a,b):
    if(a>b):
        small=b
    else:
        small=a
    for i in range(1,small+1):
        if((a%i==0) and (b%i==0)):
            h=i
    return h
print("Enter two number \n============")
x=int(input("First number "))
y=int(input("Second number "))
print("HCF of ",x," and ",y," = ",gcd(x,y))