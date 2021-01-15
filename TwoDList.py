arr1=[[1,1,1],[1,1,1],[1,1,1]]
for i in range(0,3):
    for j in range(0,3):
        print(arr1[i][j]," ",end="")
    print("\n")

arr2=[[2,2,2],[2,2,2],[2,2,2]]
for i in range(0,3):
    for j in range(0,3):
        print(arr2[i][j]," ",end="")
    print("\n")
    
arr3=[[0,0,0],[0,0,0],[0,0,0]]
for i in range(0,3):
    for j in range(0,3):
        arr3[i][j]=arr1[i][j]+arr2[i][j]
for i in range(0,3):
    for j in range(0,3):
        print(arr3[i][j]," ",end="")
    print("\n")

