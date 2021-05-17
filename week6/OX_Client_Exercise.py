import socket

def print_table(msg):
    #os.system("cls")
    print ("")
    print (" "+str(msg[0])+" | "+str(msg[1])+" | "+str(msg[2])+" ")
    print (" "+str(msg[3])+" | "+str(msg[4])+" | "+str(msg[5])+" ")
    print (" "+str(msg[6])+" | "+str(msg[7])+" | "+str(msg[8])+" ")
    print ("") 

def check():
    global count
    global msg
    if (msg[0] == msg[1]) and (msg[1] == msg[2]):         
        if (msg[0] == 'x'):
            print ("Client WIN !!!!!!!!!!!!!!")            
        if (msg[0] == 'o'):
            print ("Server WIN !!!!!!!!!!!!!!")
        count = 10        
        input()                  
    if (msg[3] == msg[4]) and (msg[4] == msg[5]):        
        if (msg[3] == 'x'):
            print ("Client WIN !!!!!!!!!!!!!!")
        if (msg[3] == 'o'):
            print ("Server WIN !!!!!!!!!!!!!!")
        count = 10
        input()          
    if (msg[6] == msg[7]) and (msg[7] == msg[8]):
        if (msg[6] == 'x'):
            print ("Client WIN !!!!!!!!!!!!!!")            
        if (msg[6] == 'o'):
            print ("Server WIN !!!!!!!!!!!!!!")
        count = 10        
        input()                      
    if (msg[0] == msg[3]) and (msg[3] == msg[6]):        
        if (msg[0] == 'x'):
            print ("Client WIN !!!!!!!!!!!!!!")
            
        if (msg[0] == 'o'):
            print ("Server WIN !!!!!!!!!!!!!!")
        count = 10        
        input()                  
    if (msg[1] == msg[4]) and (msg[4] == msg[7]):
        if (msg[1] == 'x'):
            print ("Client WIN !!!!!!!!!!!!!!")            
        if (msg[1] == 'o'):
            print ("Server WIN !!!!!!!!!!!!!!")
        count = 10        
        input()      
    if (msg[2] == msg[5]) and (msg[5] == msg[8]):        
        if (msg[2] == 'x'):
            print ("Client WIN !!!!!!!!!!!!!!")
            
        if (msg[2] == 'o'):
            print ("Server WIN !!!!!!!!!!!!!!")
        count = 10        
        input()                  

    if (msg[0] == msg[4]) and (msg[4] == msg[8]):
        if (msg[0] == 'x'):
            print ("Client WIN !!!!!!!!!!!!!!")            
        if (msg[0] == 'o'):
            print ("Server WIN !!!!!!!!!!!!!!")
        count = 10        
        input()                  
    if (msg[2] == msg[4]) and (msg[4] == msg[6]):
        if (msg[2] == 'x'):
            print ("Client WIN !!!!!!!!!!!!!!")            
        if (msg[2] == 'o'):
            print ("Server WIN !!!!!!!!!!!!!!")
        count = 10        
        input()                       


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

msg = ['1','2','3','4','5','6','7','8','9']
arr = ['1','2','3','4','5','6','7','8','9']

print ("Welcome to XO Game")
print ("")
while True:
    server = input ("Connect Server (ip address or hostname) : ")
    port = int(input("Connect Server (port number) : "))
    try:
        s.connect((server, port))
    except:
        print("Can't Connect to Server")
        pass
    else:
        break

def clientPlay():
    global msg    
    global count
    count+=1
    while True:
        tmp = input ("Client (x) : ")
        if tmp not in arr:
            print("Please input a number between 1 and 9")
        else:
            if(msg[int(tmp)-1]) == 'x' or (msg[int(tmp)-1]) == 'o':
                print("Can't input here")
            else:
                (msg[int(tmp)-1]) = 'x'
                break
    s.send(tmp.encode('ascii'))
    print_table(msg)
    check()
    if count == 9:
        print("DRAW!")
    else:
        print ("Please Wait !!!")    
    
def serverPlay():
    global msg
    global count
    count+=1
    tmp = s.recv(20)
    (msg[int(tmp)-1]) = 'o'
    print_table(msg)
    check()
    if count == 9:
        print("DRAW!!!")

count = 0
print_table(msg)
clientPlay()
serverPlay()                
clientPlay()
serverPlay()                
clientPlay()
serverPlay()                
clientPlay()
serverPlay()                
clientPlay()
s.close()
print("Disconnected")



