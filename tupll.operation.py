##Used to show Calendar of the month.
import calendar
y=int(input("Enter Year"))
m=int(input("Enter month"))
print(calendar.month(y,m))
print((1,2,3)+(4,5,6))
print(("Hello",)*3)

print("All these are Tuple function and method")
t1=(1,2,3)
print(len(t1))
print(max(t1))
print(min(t1))
print(t1)
list1=[8,9,10]
t2=tuple(list1)
print(t2)