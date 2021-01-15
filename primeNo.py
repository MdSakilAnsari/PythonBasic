num=int(input("enter a number : "))
if(num>1):
    for i in range(2,num):
        if(num%i)==0:
            print("No is not prime :{0}".format(num))
            print(i," time",num//i," is :{0} ".format(num))
            break
    else:
        print("No is prime :{0}".format(num))
else:
    print("No is invalid :{0}".format(num))
               