##Display series of armstrong numbers and display the total no. of armstrong no.in that series
def findArmstrome(s,e):
    c=0
    for num in range(s,e+1):
        temp=num
        a=0
        while(temp>0):
            r=temp%10
            a+=r**3
            temp//=10
        if(num==a):
            c+=1
            print(num," ",end="")
    print("\nNumber of amstrome number bitween {0} To {1} = {2}".format(s,e,c))
start=int(input("Enter start point "))
end=int(input("Enter end point "))
result=findArmstrome(start,end)
