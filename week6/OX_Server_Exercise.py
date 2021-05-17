import socket

def print_table(msg):
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

def clientPlay():
    global msg    
    global count
    try:
        count+=1
        #print_table(msg)
        tmp = c.recv(20)
        (msg[int(tmp)-1]) = 'x'
        print_table(msg)
        check()
        if count == 9:
            print("DRAW!!!")
    except:
        print("Client disconnected")
        
def serverPlay():
    global msg
    global count
    count+=1
    while True:
        tmp = input ("Server (o) : ")
        if tmp not in arr:
            print("Please input a number between 1 and 9")
        else:
            if(msg[int(tmp)-1]) == 'x' or (msg[int(tmp)-1]) == 'o':
                print("Can't input here")
            else:
                (msg[int(tmp)-1]) = 'o'
                break
    c.send(tmp.encode('ascii'))
    print_table(msg)
    check()
    if count == 9:
        print("DRAW!")
    else:
        print ("Please Wait !!!")

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
ip = socket.gethostbyname(host)
port = 9999
serversocket.bind((host, port))
serversocket.listen(5)

while True:
    msg = ['1','2','3','4','5','6','7','8','9']
    arr = ['1','2','3','4','5','6','7','8','9']
    print ("Welcome to XO Game")
    print ("")
    print ("hostname   : "+host)
    print ("ip address : "+ip)
    print ("")
    
    while True:
        try:
            c,addr = serversocket.accept()
            count = 0
            clientPlay()
            serverPlay()                    
            clientPlay()
            serverPlay()                    
            clientPlay()
            serverPlay()                    
            clientPlay()
            serverPlay()                    
            clientPlay()               
            c.close()
            print(str(addr) + " exit game\n")    
            break
        except:
            print("Client disconnected")
            break


