class university:
    uname="LPU"
    def univ(self):
        return self.uname
class section:
    sec="D1E37"
    def sect(self):
        return self.sec
class secmentor:
    men="Kumar Vishal"
    def mentor(self):
        return self.men
class student(university,secmentor,section):
    def name(self):
        return "Md Sakil"
    def reg(self):
        return "11812524"
s=student()
print("Name : "+s.name())
print("Reg : "+s.reg())
print("University : "+s.univ())
print("Section : "+s.sect())
print("Mentor : "+s.mentor())


