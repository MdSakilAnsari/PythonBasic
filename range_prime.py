start=int(input("Enter starting range "))
end=int(input("Enter Ending range "))
count=0
for num in range(start,end+1):
    flag=1
    for i in range(2,num):
        if(num%i==0):
            flag=0
            break
    if flag==1:
        print(num," ",end=" ")
        count+=1
print("total =", count)
    
    
  
