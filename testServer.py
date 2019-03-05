import socket, time, signal
from threading import Thread

#--------------------------------------------------
#Initialize the Server
#--------------------------------------------------
clients = {}#stores new clients
addresses = {}#stores new clients addresses
BUFSIZ = 1024#Change this value to change the buffersize of sockets

server = socket.socket()#server is now socket type and can receive/send through sockets
host = '192.168.0.44'#my internal IP
#host = socket.gethostname()
port = 50000#Port to be used for external access to my server
server.bind((host,port))#Bind the socket type to host/port

#--------------------------------------------------
#Server Functions for listening, sending, handling, and receiving
#--------------------------------------------------
def portListener():#listen for new clients
    while True:
        client, clientAddress = server.accept()#accept the new TCP connection
        print("%s:%s has connected." % clientAddress)#Notify server of new connection
        client.send(bytes("Welcome to ugoChat!\r\r", "utf8")) 
        client.send(bytes("Now type your name and press enter!","utf8"))#prompt client
        addresses[client] = clientAddress#store clients address in list
        Thread(target=handleClient, args=(client,)).start()#initialize new thread               

def handleClient(client):#handle client interaction
    name = client.recv(BUFSIZ).decode("utf8")#receive the clients name
    greeting = 'Welcome %s! to exit ugoChat simply type {exit}.' % name
    client.send(bytes(greeting, "utf8"))#instructions on how to leave
    msg = "%s has joined the chat!" % name
    broadcast(bytes(msg, "utf8"))#Notify all other users of new client
    clients[client] = name#Store the clients selected name
    while True:#loop in charge of allowing the client pass messages
        msg = client.recv(BUFSIZ)#receive message from client
        if msg != bytes("{exit}", "utf8"):
            broadcast(msg, name+": ")#Send message to all other users
        else:#user wishes to disconnect
            client.close()#remove clients socket connection
            del clients[client]#delete client from list of clients
            broadcast(bytes("%s has left the chat." % name, "utf8"))#broadcast exit
            break#end of while loop

def broadcast(msg, prefix=""):#handles the broadcasting of messages to all users
    for sock in clients:#iterate through all clients receiving socket
        sock.send(bytes(prefix, "utf8")+msg)#send the msg to each client
#--------------------------------------------------
#main()
#--------------------------------------------------
if __name__ == "__main__":
    server.listen(5)#listen to a max of 5 connections
    print("Awaiting new ugo...")
    listenerThread = Thread(target=portListener)
    listenerThread.start()
    listenerThread.join()
    server.close()
