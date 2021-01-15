class emp:
    empdet={}
    name=[]
    id=[]
    def setDetail(self):
        for i in range (0,3):
            self.empname=input("Enter name : ")
            self.name.append(self.empname)
            self.empid=input("Enter Id : ")
            self.id.append(self.empid)
            self.empdet[self.empname]=self.empid
    def getDetail(self):
        print("Name","\t","Id")
        for i in range(0,3):
            print(self.name[i],"\t",self.id[i])
        print(self.empdet)
e=emp()
e.setDetail()
e.getDetail()
