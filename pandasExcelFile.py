import pandas as pd
from pandas import ExcelWriter
list1=[[1,2,3],['A','B','C']]
df=pd.DataFrame(list1)
writer=ExcelWriter('sampl.xlsx')
df.to_excel(writer,sheet_name='sheet1',startcol = 3)
writer.save()
