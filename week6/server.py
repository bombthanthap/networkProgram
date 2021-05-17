##import os
from socket import *


# READ_FILE config
##file = open("config.txt","r")
##text = []
##for i in file:
##    name, value = i.split()
##    text.append(value)
##file.close()
##
##host = text[0]
##port = int(text[1])
# END READ_FILE

host = gethostbyname(gethostname())
port = 4444

buffer_size = 1024
address = (host,port)

server = socket(AF_INET,SOCK_STREAM)
server.bind(address)
server.listen(5)

myaccount = "5930300232"
print("Server Address : " + host + "\nServer Port : " + str(port))
WelcomeMessage = "Hello " + myaccount + "\nTell me, who are you?"

while True:
    print("Waiting for connection...")
    client,address = server.accept()
    print("Connect from : ",address)
    client.send(str.encode(WelcomeMessage))

    while True:
        try:
            message = bytes.decode(client.recv(buffer_size))
        except:
            print("Client has disconnected")
            break
        if not message:
            print("Client disconnected")
            client.close()
            break
        else:
            print("Client said : " + message)
            try:
                client.send(str.encode(input(" > ")))
            except:
                print("Client has disconnected")
                break
