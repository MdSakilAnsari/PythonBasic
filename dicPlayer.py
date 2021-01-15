max_value=0
diff=0
IPL1={}
IPL2={}
Score={}
perform={}
choice=int(input("Enter no of element should be added in dictionary : "))
for i in range(0,choice):
    key=input("Enter key name {0} out of {1} : ".format(i+1,choice))
    value1=input("Enter score of IPL-1 {0} out of {1} : ".format(i+1,choice))
    value2=input("Enter score of IPL-2 {0} out of {1} : ".format(i+1,choice))
    IPL1[key]=value1
    IPL2[key]=value2
for x,y in IPL1.items():
    value=int(IPL1[x])+int(IPL2[x])
    if max_value < value:
        key=x
        max_value=value
Score[key]=max_value
print(IPL1)
for x,y in IPL1.items():
    val=int(IPL2[x])-int(IPL1[x])
    if diff < val:
        key=x
        diff=val
perform[key]=diff
print(IPL2)
print("Maximum score made by",Score)
print("IPL2 Performance was better than IPL1",perform)
