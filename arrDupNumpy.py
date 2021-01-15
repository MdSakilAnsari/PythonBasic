import numpy as np
arr=np.array([12,7,3,5,7,8,3,0,7,0,0])
dup=[]
garb=max(arr)+100
print(arr)
for i in range(arr.size):
    d=1
    for j in range (i+1,arr.size):
        if arr[i]==arr[j] and arr[i]!=garb:
            d+=1
            arr[j]=garb
    if d!=1:
        print("{0} found {1} times in series".format(arr[i],d))
        dup.append(arr[i])
print(arr)
print(dup)

