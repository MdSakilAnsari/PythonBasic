import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
data={'x':[22,65,7,45,13,16,36,92,17,20,50,25,43,19],'y':[45,23,21,41,9,43,14,24,36,75,45,7,12,55]}
df=pd.DataFrame(data,columns=['x','y'])
kmeans=KMeans(n_clusters=5).fit(df)
centroids=kmeans.cluster_centers_
print(centroids)
plt.scatter(df['x'],df['y'],c='green')
plt.scatter(centroids[:,0],centroids[:,1],c='red')
plt.show()
