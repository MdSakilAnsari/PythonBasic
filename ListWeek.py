day=["Mon","Tues","Wed","Thur","Fri","Sat","Sun"]
value=[6,1,4,6,2,7,3]
value.sort()
print("1 :To Monday\n2 :To Tuesday\n3 :To Wednesday\n4 :To Thursday\n5 :To Friday\n6 :To Saturday\n7 :To Sunday")
while(True):
    ch=int(input("Enter your choice : "))
    if(ch==1):
        print(day(1))
    elif(ch==2):
        print(day(2))
    elif(ch==3):
        print(day(3))
    elif(ch==4):
        print(day(4))
    elif(ch==5):
        print(day(5))
    elif(ch==6):
        print(day(6))
    elif(ch==7):
        print(day(7))
    else:
        break
