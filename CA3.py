class Product:
    def setName(self,name):
        self.pName=name
        return self.pName
class Brand:
    def brandName(self,name):
        self.bName=name
        return self.bName
class Price(Product,Brand):
    def setPrice(self,amt):
        self.priceAmt=amt
        return self.priceAmt
    def setQty(self,qt):
        self.itemQty=qt
        return self.itemQty
    def calculatePrice(self):
        return self.itemQty*self.priceAmt
p=Price()
print("Product Name : ",p.setName("Male Watch"))
print("Brand Name : ",p.brandName("Titan"))
print("Marked Price : ",p.setPrice(1200))
print("Qty : ",p.setQty(2))
print("Paid Amount : ",p.calculatePrice())
    