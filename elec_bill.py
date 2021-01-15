unit=int(input("Enter consumed unit "))
if unit>100:
    bill=unit*6.95
else:
    bill=unit*5.95
print(bill)
