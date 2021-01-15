import pandas as pd
list1=[]
li=["","",0,0,0,0]
n=int(input("Enter number of record should be added : "))
print('Name','Registration','CA-1','CA-2','CA-3')
for i in range(0,n):
    name,reg,c1,c2,c3=input().split()
    m1=int(c1)
    m2=int(c2)
    m3=int(c3)
    if  m1<m2 and m1<m3:
        tm=(m2+m3)/2
    elif m2<m1 and m2<m3:
        tm=(m1+m3)/2
    else:
        tm=(m1+m2)/2
    li[0]=name
    li[1]=reg
    li[2]=c1
    li[3]=c2
    li[4]=c3
    li[5]=tm
    list1.append(li)
df=pd.DataFrame(list1,columns=['Name','Registration','CA-1','CA-2','CA-3','Total'])
print(df)

