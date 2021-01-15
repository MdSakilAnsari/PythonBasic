class bank:
    ia=5000
    def amount(self):
        print("Initial amount : ",self.ia)
class SBI(bank):
    roi=7
    def famount(self):
        self.famt=self.ia+((self.ia*self.roi)/100)
        print("According to SBI : ",self.famt)
    
class PNB(bank):
    roi=6.5
    def famount(self):
        self.famt=self.ia+((self.ia*self.roi)/100)
        print("According to PNB : ",self.famt)
class ICICI(bank):
    roi=10
    def famount(self):
        self.famt=self.ia+((self.ia*self.roi)/100)
        print("According to ICICI : ",self.famt)
s=SBI()
p=PNB()
i=ICICI()

s.amount()
s.famount()
p.amount()
p.famount()
i.amount()
i.famount()
