import pandas as pa
import matplotlib.pyplot as plt
data={'Name':['Sakil','Rohit','Sanu'],'Age':[22,24,26],'Score':[120,95,135]}
df=pa.DataFrame(data,columns=['Name','Age','Score'])
df.plot(x='Name',y='Score',kind='bar')
plt.show()