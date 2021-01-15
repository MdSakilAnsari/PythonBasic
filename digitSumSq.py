def digitSum(num):
    sq=1
    sum=0
    while(num>0):
        r=num%10
        sq=r**2
        sum+=sq
        num//=10
    return sum
num=int(input("enter a number "))
result=digitSum(num)
print("Sum of square digit = :{}".format(result))    
        
               