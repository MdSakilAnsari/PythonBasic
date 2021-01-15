#Create a scatter plot and showing the co-variation between columns of your choice.Label the axix.
import pandas as pa
from numpy import cov
val=pa.read_csv("Co_var.csv")
df=pa.DataFrame(val)
print(df)
list1=[2.1,2.5,3.3,4.0]
list2=[8,10,9,12]
cv=cov(list1,list2)
print(cv)


