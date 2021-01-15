
a=0
b=1
print(a,end=",")
print(b,end=",")  
for i in range(3,11):
    c=a+b
    print(c,end=",")
    (a,b)=(b,c)
    
