class faculty:
    salary=30000
    def showSalary(self):
        print("Salary of class Faculty : ",self.salary)
class science(faculty):
    bonus=2000
    def calSalary(self):
        self.sal=self.bonus+self.salary
        print("Salary of class Science : ",self.sal)
class computer(science):
    allowance=1000
    def calcSalary(self):
        self.total=self.allowance+self.sal
        print("Salary of class Computer : ",self.total)
comp=computer()
comp.showSalary()
comp.calSalary()
comp.calcSalary()
