class Calculation1:  
    def Summation(self,a,b): 
        print("Hiii") 
        return a+b;  
class Calculation2:  
    def Summatio(self,a,b):  
        print("Hello") 
        return a*b;  
class Derived(Calculation1,Calculation2):  
    def Divide(self,a,b):  
        return a/b;  
d = Derived()  
print(d.Summation(10,20))  
print(d.Summatio(20,30))  
print(d.Divide(20,20))  