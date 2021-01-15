list=['sakilal','gold']
list2=[]##Creating empty list

size=len(list)
for i in range(0,size):
    list2.append(list[i].upper())##Converting  in upper case of list item and appending it onto list2
print(list2)##Printing list value of List2
print(list[0].find("l"))##It will find first occurance of character 'l'
print(list[0].replace('s','w'))##It will replace character 's' by 'w'