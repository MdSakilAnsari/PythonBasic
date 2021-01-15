# Numpy is a library package of array used for array manipulation for the purpose of scientific and numerical calculations.
import numpy as np
s=0
num=np.array([1,2,3,4,5,6,7,8,9])
num1=np.array([1,2,3,4,5,6,7,8,9])
for i in range (0,num.size):#To find length of an array in another method "np.size(array_name)"
    s+=num[i]
print(num)
print(num[4:8])#It will print from 4th index of array till 7th.
print(s)
num=num+1#Arithmetic operation with array elements It will increments all elements by one.
print(num1+num)
print(num.ndim)#To check diamension of an array
print(num.shape)#To print number of columns
print(num.dtype)#To print data type of an array
