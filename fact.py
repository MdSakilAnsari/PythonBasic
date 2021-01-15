num=int(input("enter a number "))
factorial=1
if(num<0):
    print("Number can't be negative")
elif(num==0):
    print(num," Factorial = 1")
else:
    for i in range(1,num+1):
       factorial=factorial*i
    print(num," Factorial :{}".format(factorial))
        
               