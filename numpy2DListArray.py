import pandas as pd
import numpy as np
listId=[]
listName=[]
sizes=int(input("Enter number of record should be added : "))
for i in range(sizes):
    listId.append(input("Enter User_Id for users {0} out of {1} ".format(i+1,sizes)))
    listName.append(input("Enter User_Name for users {0} out of {1} ".format(i+1,sizes)))
arr=np.array([listId,listName])
df=pd.DataFrame(arr)
print(df)