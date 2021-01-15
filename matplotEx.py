from matplotlib import pyplot as plt 
import pandas as pa
x = [2008,2009,2010,2011,2012] 
y = [120,345,204, 262,445] 
df=pa.DataFrame([x,y])
plt.scatter(x,y)
plt.show()

#plt.plot(x,y)
#plt.bar(x,y)
#plt.show()