list=['1234','Hello','hi','12.6',' ']
size=len(list)
count=0
sp=0
dg=0
nu=0
de=0
for i in range(0,size):
    if(list[i].isalpha()):
        count+=1
    if(list[i].isspace()):
        sp+=1
    if(list[i].isdigit()):
        dg+=1
    if(list[i].isdecimal()):
        de+=1
    if(list[i].isnumeric()):
        nu+=1
print("Number of String {0} Digit {1} space {2} decimal {3} numeric {4}".format(count,dg,sp,de,nu))

