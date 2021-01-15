#CGPA Calculator
CA_Total=100
CA_Wtg=25
MTE_Total=40
MTE_Wtg=20
ETE_Total=70
ETE_Wtg=50
C_code=input("Enter course code ")
CA_obt=int(input("CA mark obtain "))
MTE_obt=int(input("MTE mark obtain "))
ETE_obt=int(input("ETE mark obtain "))
At=int(input("Enter Attendance mark "))
CA_mark=(CA_obt*CA_Wtg)/CA_Total
MTE_mark=(MTE_obt*MTE_Wtg)/MTE_Total
ETE_mark=(ETE_obt*ETE_Wtg)/ETE_Total
total=CA_mark+MTE_mark+ETE_mark+At
print("Mark Obtain for ",C_code," ",total, end=" ")
print("Final CGPA =",total/10)