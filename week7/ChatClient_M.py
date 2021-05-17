'''Chat Client for a multi-client chat room'''
from socket import *
BUFSIZE = 4096      
server = socket(AF_INET, SOCK_STREAM)
HOST = input("Please enter hostname or IP Address to connect : ")
PORT = int(input("Please enter port number to connect : "))
while True:
    try:
        ADDRESS = (HOST, PORT)
        server.connect(ADDRESS)
    except:
        HOST = input("Please enter hostname or IP Address to connect : ")
        PORT = int(input("Please enter port number to connect : "))
    else :
        break
    
messageFromServer = bytes.decode(server.recv(BUFSIZE))
print(messageFromServer)
name = input('Enter your name: ')
userName = str.encode(name)
server.send(userName)
while True:
    receiveMessage = bytes.decode(server.recv(BUFSIZE))
    if not receiveMessage:
        print('Server disconnected')
        break
    print(receiveMessage)
    sendMessage = input('> ')
    server.send(str.encode(sendMessage))
    if sendMessage == "bye" :
        print('Left Chat')
        break    
server.close()
