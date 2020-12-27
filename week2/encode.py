import hashlib
import json

with open('userdata.json','r') as j:
    userdata = json.load(j)
    
##    print(userdata)
##    print(userdata["Password"])
    
##3334edaeed449ab2cf8a55b95817532780a0312ce91699e3a7d844db792e3e45

while(1):
    plainusername = input("Please input Username : ")
    plainpassword = input("Please input password : ")
    hashpassword = hashlib.sha256(plainpassword.encode('utf-8')).hexdigest()

    if((userdata["Username"] == plainusername ) and (userdata["Password"] == hashpassword)):
        print(userdata["Fullname"])
        print(userdata["Email"])
        print(userdata["TelNo"])
        break
    else:
        print("Wrong username or password!")
        print("Please Try agian")


##print(hashpassword)
