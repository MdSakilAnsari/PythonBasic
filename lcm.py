def gcd(a,b):
    if(a==0):
        return b
    return gcd(b%a,a)
def findLcm(a,b):
    return (a*b)/gcd(a,b)
print("Enter two number to find LCM \n================")
x=int(input("First number "))
y=int(input("Second number "))
print("LCM of ",x," and ",y," = ",findLcm(x,y))