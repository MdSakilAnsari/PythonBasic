list1=[]
list2=[]
list3=[]
lv1=int(input("Enter number of element in list1 : "))
for i in range(0,lv1):
    list1.append(int(input()))
lv2=int(input("Enter number of element in list2 : "))
for i in range(0,lv2):
    list2.append(int(input()))
for i in range(0,lv1):
    for j in range(0,lv2):
        if list1[i]==list2[j]:
            list3.append(list1[i])
print("Element of List1 : ",list1)
print("Element of List2 : ",list2)
print("Common Elements in both List : ",list3)