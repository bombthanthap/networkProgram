from ftplib import FTP
import os,sys

##ftp = FTP('158.108.97.18')
##ftp.login(user = 'ST03603423',passwd = '03603423')
##id usertest
##passwd 1234

##----- read file ----------------------------------------
try:
    name = open("user.txt","r")
except FileNotFoundError:
    print("No file")
    sys.exit(1)

ar = []
for line in name:
    a,data = line.split()
    ar.append(data)

ip = ar[0]
user = ar[1]
password = ar[2]
std_id = ar[3]
name.close()
##print(ar)

##----- Connect Server ------------------------------------
try:
    ftp = FTP(ip)
    ftp.login(user =user,passwd =password)
    print("===== User Conected =====")
except:
    print("IP or user or passwd wrong can't connected")
    sys.exit(1)
##ftp.retrlines('LIST')


##---------- Functional ---------------
def downloadFile():
## filename = 'CD NetProScores.txt'
    filename = 'NetProScore.txt'
    localfile = open(filename,'wb')
    ftp.retrbinary('RETR '+filename,localfile.write,1024)
    localfile.close()

def uploadFile():
    try:
        ftp.cwd('5930300232')
    except:
        ftp.mkd('5930300232')
        ftp.cwd('5930300232')
    filename = '5930300232.txt'
    ftp.storbinary('STOR '+filename,open(filename,'rb'))
    print("***** Upload Success *****")


downloadFile()

##----- find Score -------------------------
try:
    name = open("NetProScore.txt","r")
except FileNotFoundError:
    print("No file")
    sys.exit(1)

score = []
ID = []
for i in name:
    NO,ID,P1,P2 = i.split()
    if ID == std_id:
        mysc = int(P1)+int(P2)
    score.append(int(P1)+int(P2))
name.close()
##print(score)
##print(mysc)

maxscore = max(score)
minscore = min(score)
avgscore = sum(score)//len(score)

##----- build 5930300232.txt --------------------------------------
name = open("5930300232.txt","w",encoding="utf-8")
name.write("Highest Score = "+str(maxscore)+" คะแนน"+"\n")
name.write("Lowest Score = "+str(minscore)+" คะแนน"+"\n")
name.write("Average Score = "+str(avgscore)+" คะแนน"+"\n")
name.write("รหัส 5930300232 ได้คะแนนรวม = "+str(mysc)+" คะแนน"+"\n")
name.write("ได้น้อยกว่าคะแนนสูงสุด = "+str(maxscore-mysc)+" คะแนน"+"\n")
name.write("ได้มากกว่าคะแนนต่ำสุด = "+str(mysc-minscore)+" คะแนน"+"\n")
name.write("ได้มากกว่าคะแนนเฉลี่ย = "+str(mysc-avgscore)+" คะแนน"+"\n")
name.close()

##----- Upload to Server ------------------------------------------
uploadFile()
##ftp.retrlines('LIST')

ftp.close()
