import numpy as ps
import pandas as pd
rows=int(input("Enter number of row : "))
cols=int(input("Enter number of columns : "))
twoD=ps.array([["            " for i in range(cols)] for j in range(rows)])
for a in range(rows):
    for b in range(cols):
        twoD[a][b]=input("Enter  value for row {0},{1} : ".format(a,b))
print(twoD)
df=pd.DataFrame(twoD,index=['name','id'],columns=['col','col2','col3'])
print(df)
