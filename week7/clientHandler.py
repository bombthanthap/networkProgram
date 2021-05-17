from threading import Thread

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
            message = bytes.decode(self._client.recv(BUFSIZE))
            if not message:
                print(str(self._address) + " disconnected")
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
