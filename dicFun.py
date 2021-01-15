IPL1={}
IPL2={}
total={}
choice=int(input("Enter no of element should be added in dictionary : "))
for i in range(0,choice):
    key=input("Enter key name {0} out of {1} : ".format(i+1,choice))
    value1=input("Enter score of IPL-1 {0} out of {1} : ".format(i+1,choice))
    value2=input("Enter score of IPL-2 {0} out of {1} : ".format(i+1,choice))
    IPL1[key]=value1
    IPL2[key]=value2
for x,y in IPL1.items():
    value=int(IPL1[x])+int(IPL2[x])
    total[x]=value
print(IPL1)
print(IPL2)
print(total)
print(max(total,key=total.get))
print(max(total.values()))
