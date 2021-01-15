dic={}
choice=int(input("Enter no of element should be added in dictionary  : "))
for i in range(0,choice):
    key=input("Enter key name {0} out of {1} : ".format(i+1,choice))
    value=input("Enter Value {0} out of {1} : ".format(i+1,choice))
    dic[key]=value
print(dic)
