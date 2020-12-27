import os

##os.getcwd()
##f = open("AllScore.txt")
##f.read()

sum = 0

p = 0
a = 0
bp = 0
b = 0
cp = 0
c = 0

input = open("AllScore.txt")

for i in input:
##    print(i.strip())
    Q,W,E,R,T = i.split()
    sum = int(E)+int(R)+int(T)
    p += 1
##    print("SUM: ",sum)
    if(sum>=80):
        a +=1
    elif(sum>=75 and sum <=79):
        bp +=1
    elif(sum>=70 and sum <=74):
        b +=1
    elif(sum>=60 and sum <=69):
        cp +=1
    elif(sum<60):
        c +=1
input.close()

##print("people:",p)
##print("A:",a)
##print("B+:",bp)
##print("B:",b)
##print("C+:",cp)
##print("C:",c)


##-----WRITE-----
os.chdir("d://")

os.mkdir("5930300232")
os.chdir("d://5930300232")

out = open("ReportGrade.txt","w",encoding="utf-8")
out.write("จำนวนนักศึกษาทั้งหมด ="+str(p)+"คน"+"\n")
out.write("จำนวนคนที่ได้ A ="+str(a)+"คน"+"\n")
out.write("จำนวนคนที่ได้ B+ ="+str(bp)+"คน"+"\n")
out.write("จำนวนคนที่ได้ B ="+str(b)+"คน"+"\n")
out.write("จำนวนคนที่ได้ C+ ="+str(cp)+"คน"+"\n")
out.write("จำนวนคนที่ได้ C ="+str(c)+"คน"+"\n")
out.close()


##------READ-----
##writ = open("output.txt")
##for i in writ:
##    print(i)
##writ.close()
