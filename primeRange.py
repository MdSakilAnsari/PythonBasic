start=int(input("enter a start point "))
end=int(input("enter a end point "))
sum=0
if(start>1):
    for num in range(start,end+1):
        flag=1
        for i in range(2,num):
                if(num%i)==0:
                    flag=0
                    break
        if flag==1:
            print("{0} ".format(num),end="")
            sum+=num        
    print("Sum = {} ".format(sum))       
else:
    print("Invalid starting point :{}".format(start))
               