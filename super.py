class university:
    def __init__(self):
        print("University class Called")
    uname="LPU"
    def univ(self):
        return self.uname
class section:
    def __init__(self,x):
        print("Section class Called : ",x)
    sec="D1E37"
    def sect(self):
        return self.sec
class secmentor:
    def __init__(self):
        print("Mentor class Called")
    men="Kumar Vishal"
    def mentor(self):
        return self.men
class student(section,university,secmentor):
    def __init__(self,a,b):
        super().__init__(b)
        print("Student1 name: ",a)
    def name(self):
        return "Md Sakil"
    def reg(self):
        return "11812524"
s=student("JOshi","sanu")
print("Name : "+s.name())
print("Reg : "+s.reg())
print("University : "+s.univ())
print("Section : "+s.sect())
print("Mentor : "+s.mentor())


