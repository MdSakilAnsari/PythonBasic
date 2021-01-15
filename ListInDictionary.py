import pandas as ps
d={'player':['Sakil','Rohit','Sanu'],
    'Age':[12,23,45],
    'Score':[100,122,93]}
pd=ps.DataFrame(d)#It will add into dataframe all columns of dictionary or List.
print(pd)
p=ps.DataFrame(d,columns=['Age','Score'])#It will add into dataframe two columns Age and Score Only.
print(p)