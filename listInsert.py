list=[1,2,3,4,5]
n=int(input("Enter size : "))
for j in range(0,n):
    i=int(input("Enter value {0} : ".format(j+1)))
    list.append(i)##Adding element using append() method at the end of list.
print("Maximum value is : ",max(list))##finding maximum value using max() function
print("Minimum value is : ",min(list))##finding minimum value using min() function
print("Sum of List element : ",sum(list))##finding sum value using sum() function
print(list)