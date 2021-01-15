import pandas as pd
import numpy as np
arr=np.array([[1,2,3],['A','B','C'],["Sakil","Rohit","Sanu"]])
df=pd.DataFrame(arr,index=['ID','Code','Name'],columns=['Users1','Users2','Users3'])
print(df)