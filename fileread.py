files_Name=input("Enter file name to read : ")
fobject=open(files_Name+".pdf","r")
for i in fobject:
    print(i)
fobject.close()