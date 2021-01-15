p1=int(input("Enter mark of paper-1 "))
gp1=int(input("Enter weightage "))
p2=int(input("Enter mark of paper-2 "))
gp2=int(input("Enter grade-point "))
p3=int(input("Enter mark of paper-3 "))
gp3=int(input("Enter grade-point "))
p4=int(input("Enter mark of paper-4 "))
gp4=int(input("Enter grade-point "))
p5=int(input("Enter mark of paper-5 "))
gp5=int(input("Enter grade-point "))
sumofmark=(p1*gp1)+(p2*gp2)+(p3*gp3)+(p4*gp4)+(p5*gp5)
sumgrade=gp1+gp2+gp3+gp4+gp5
tot=(sumofmark/sumgrade)/10
print("Your CGPA ",tot)
