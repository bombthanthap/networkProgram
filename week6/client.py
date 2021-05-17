from socket import *

##host = gethostname()
##address = (host,port)
##port = 4444

buffer_size = 1024

server = socket(AF_INET,SOCK_STREAM)

while True:
    host = input("Input Server IP number: ")
    port = int(input("Input Server PORT number: "))
    address = (host,port)
    try:
        server.connect(address)
    except:
        print("**************** \nCan't connected \nPlease try agian \n****************")
        pass
    else:
        break

messageFromServer = bytes.decode(server.recv(buffer_size))
print(messageFromServer)

while True:
    try:
        message = input(" > ")
        server.send(str.encode(message))
        if not message:
            break
        reply = bytes.decode(server.recv(buffer_size))
        if not reply:
            print("Server disconnected")
            break
        print("Server said : " + reply)
    except:
        print("Server disconnected")
        break
server.close()
print("Left chat")
