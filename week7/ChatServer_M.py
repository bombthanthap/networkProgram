
'''Chat Server for a multi-client chat room''' # remark at first character
from socket import *
from threading import Thread
import threading
from time import ctime 


'''Chat Database Script'''
class chatRecord():
    def __init__(self):
        self.data = []

    def addMessage(self, message):
        self.data.append(message)

    def getMessage(self, messageID):
        if len(self.data) == 0:
            return 'No message yet!'
        elif messageID == 0: #get all message for database
            return '\n'.join(self.data)
        elif messageID != 0: #get a chunk of message
            temp = self.data[messageID:]
            return '\n'.join(temp)
        else:
            return "\n"

class clientHandler(Thread):
    def __init__(self, client, record, address):
        Thread.__init__(self)
        self._client = client
        self._record = record
        self._address = address
    #broadcasting chat messages to all connected clients
    def broadCastingMessage(self, activeClient, message):
    #Do not send the message to server and the client who has send the message to us
        for socket in CONNECTIONS_LIST:
            if socket != server and socket != activeClient:
                try:
                    broadcastMessage = str.encode(message)
                    socket.send(broadcastMessage)
                except:
                    # broken socket connection may be, chat client pressed ctrl+c for example
                    print ("Client (%s) is offline" %self._address)
                    broadCastingMessage(socket, ("Client (%s) is offline" %self._address))
                    socket.close()
                    CONNECTIONS_LIST.remove(socket)

    def run(self):
        self._client.send(str.encode(WelcomeMessage))
        self._name = bytes.decode(self._client.recv(BUFSIZE))
        #Geting all messages from database and send them to client in the first time
        allMessage = self._record.getMessage(0)
        self._client.send(str.encode(allMessage))
        while True:
            try:
                message = bytes.decode(self._client.recv(BUFSIZE))
            except:
                print(str(self._address) + " disconnected")
                self._client.close()
                CONNECTIONS_LIST.remove(self._client)
                break
            if message == "bye":
                print(str(self._address) + " left chat")
                self._client.close()
                CONNECTIONS_LIST.remove(self._client)
                break
            else:
                message = ctime() + ': [' + self._name + '] -->' + message
                self._record.addMessage(message)
                #Broadcasing a new messages to every clients
                threadLock.acquire()
                self.broadCastingMessage(self._client,message)
                threadLock.release()

HOSTNAME = gethostname()
IPADDRESS = gethostbyname(gethostname())
PORT = 5000
BUFSIZE = 4096
ADDRESS = (HOSTNAME, PORT) #(127.0.0.1, 5000)
# List to keep track of all socket connections
CONNECTIONS_LIST = []
# Creating Threads Synchronization
threadLock = threading.Lock()
                             
record = chatRecord()
server = socket(AF_INET, SOCK_STREAM)
server.bind(ADDRESS)
server.listen(10)
# Add server socket to the list
CONNECTIONS_LIST.append(server)
ID = "5930300232"
WelcomeMessage = "Welcome to " +ID + "'s Chatroom"
#print(WelcomeMessage)
print ("Chat server started on hostname : " , HOSTNAME)
print ("Chat server started on IP Address : " , IPADDRESS)
print ("Chat server started on port : " + str(PORT))

while True:
        print('Waiting for connection...')
        client, address = server.accept()
        print('...connected from:', address)
        # Lock CONNECTIONS_LIST for inserting connected client
        threadLock.acquire()
        CONNECTIONS_LIST.append(client)
        # Release CONNECTIONS_LIST
        threadLock.release()
        handler = clientHandler(client, record, address)
        handler.start()
                             
