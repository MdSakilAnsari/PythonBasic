import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
data={'x':[2,3,4,5,6,7,9,0,1,2,7,8],'y':[1,2,3,4,5,7,9,7,5,3,2,8]}
df=pd.DataFrame(data,columns=['x','y'])
kmeans=KMeans(n_clusters=2).fit(df)
centroids=kmeans.cluster_centers_
print(centroids)
plt.scatter(df['x'],df['y'],c='green')
plt.scatter(centroids[:,0],centroids[:,1],c='red')
plt.show()

