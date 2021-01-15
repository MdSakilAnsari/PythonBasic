import os
Name=input("Enter Cunsumer Name : ")
Id=input("Enter Cunsumer Id : ")
Address=input("Enter Cunsumer Address : ")
cunit=input("Enter consumed unit : ")
if int(cunit)>100:
    bill=int(cunit)*4.5
else:
    bill=int(cunit)*6.2
filep=os.path.exists("bill.txt")
if filep:
    fo=open("bill.txt","a")
    fo.write("\n\nCustomer Name : "+Name+"\n"+"Customer Id : "+Id+"\n"+"Address : "+Address+"\n"+"Consumed unit : "+cunit+"\n"+"Payable amount : "+str(bill))
else:
    fo=open("bill.txt","x")
    fo.write("\nCustomer Name : "+Name+"\n"+"Customer Id : "+Id+"\n"+"Address : "+Address+"\n"+"Consumed unit : "+cunit+"\n"+"Payable amount : "+str(bill))
fo.close()





    
