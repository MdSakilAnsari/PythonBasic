List1=[]
n=int(input("Enter number of value should be added in the list : "))
for i in range(0,n):
    List1.append(input("Value {0} out of {1} : ".format(i+1,n)).split(" "))
tuple1=tuple(List1)
print(List1)
print(tuple1)