num=int(input("Enter number "))
sum=0
temp=num
while num>0:
    digit=num%10
    sum=sum+digit**3
    num=num/10
if(temp==sum):
    print("Number is armstrome")
else:
    print("Number is not armstrome")