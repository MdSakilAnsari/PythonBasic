Name=input("Enter Cunsumer Name : ")
Id=input("Enter Cunsumer Id : ")
Address=input("Enter Cunsumer Address : ")
cunit=input("Enter consumed unit : ")
if int(cunit)>100:
    bill=int(cunit)*4.5
else:
    bill=int(cunit)*6.2
fname=input("Enter Name : ")
filep=open(fname+".pdf",'w')
filep.write("Customer Name : "+Name+"\n"+"Customer Id : "+Id+"\n"+"Address : "+Address+"\n"+"Consumed unit : "+cunit+"\n"+"Payable amount : "+str(bill))
filep.close()
