import numpy as np
'''rows,cols=(6,6)
arr =np.array([[0 for i in range(rows)] for j in range(cols)])
print(arr)'''
arr1=np.array([[1,2,3],[4,5,6]])
arr=np.array([[6,5,4],[3,2,1]])
print("Elements of array1 : \n",arr1)
print("Elements of array2 : \n",arr)
#print(arr1.itemsize)It will print size of single elements
#print(arr1.nbytes) It will print size of all elements available in array
x,y=arr1.shape #It will returns number of rows and columns
s=np.array([[0 for a in range(y)] for b in range(x)])
for i in range (0,x):
    for j in range (0,y):
        s[i][j]=arr1[i][j]+arr[i][j]
print("Sum Of Arrays 1 and Arrays 2 : \n",s)

