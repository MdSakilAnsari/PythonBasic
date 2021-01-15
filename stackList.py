stack=[]
print("1 :To push element\n2 :To pop emlement\n3 :To display")
while(True):
    ch=int(input("Enter your choice : "))
    if(ch==1):
        item=int(input("Enter element : "))
        stack.append(item)
        print("Value Inserted")
    elif(ch==2):
        stack.pop()
        print("Value popped")
    elif(ch==3):
        print(stack)
    else:
        break
