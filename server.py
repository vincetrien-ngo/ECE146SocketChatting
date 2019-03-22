import socket, time, signal
from userDatabase import updateTable
from userDatabase import checkTable
from userDatabase import checkUserName
from threading import Thread

# --------------------------------------------------
# Initialize the Server
# --------------------------------------------------

clients = {}  # stores new clients
addresses = {}  # stores new clients addresses
BUFSIZ = 1024  # Change this value to change the buffersize of sockets

server = socket.socket()  # server is now socket type and can receive/send through sockets
# host = '192.168.0.44'  # my internal IP 73.235.230.212
host = '73.235.230.212'
port = 50000  # Port to be used for external access to my server
server.bind((host, port))  # Bind the socket type to host/port

# --------------------------------------------------
# Server Functions for listening, sending, handling, and receiving
# --------------------------------------------------


def portListener():  # listen for new clients
    while True:
        client, clientAddress = server.accept()  # accept the new TCP connection
        print("%s:%s has connected." % clientAddress)  # Notify server of new connection
        addresses[client] = clientAddress  # store clients address in list
        Thread(target=handleClient, args=(client,)).start()  # initialize new thread


def handleClient(client):  # handle client interaction
    loggedIn = False
    name = ""  # user has not logged in yet
    cmdNum = ""
    while not loggedIn:
        while not cmdNum:
            cmdNum = client.recv(BUFSIZ).decode("utf8")

        if cmdNum == "1":  # read command number for login attempt
            name = client.recv(BUFSIZ).decode("utf8")  # receive the clients name
            passWord = client.recv(BUFSIZ).decode("utf8")  # receive the clients password
            if checkTable(name,passWord):
                loggedIn = True
                client.send(bytes("Success", "utf8"))
            else:
                client.send(bytes("Failed", "utf8"))
        elif cmdNum == "2":  # register attempt
            userName = client.recv(BUFSIZ).decode("utf8")
            passSelect = client.recv(BUFSIZ).decode("utf8")
            if not checkUserName(userName):
                updateTable(userName,passSelect)
                client.send(bytes("Success", "utf8"))
                cmdNum = ""
            else:
                client.send(bytes("Username Taken!", "utf8"))
                cmdNum = ""
    
    time.sleep(1)
    clients[client] = name  # Store the clients selected name
    while True:  # loop in charge of allowing the client pass messages
        msg = client.recv(BUFSIZ)  # receive message from client
        if msg != bytes("{exit}", "utf8"):
            broadcast(msg, name+": ")  # Send message to all other users
        else:  # user wishes to disconnect
            client.close()  # remove clients socket connection
            del clients[client]  # delete client from list of clients
            broadcast(bytes("%s has left the chat." % name, "utf8"))  # broadcast exit
            break  # end of while loop


def broadcast(msg, prefix=""):  # handles the broadcasting of messages to all users
    for sock in clients:  # iterate through all clients receiving socket
        sock.send(bytes(prefix, "utf8")+msg)  # send the msg to each client

# --------------------------------------------------
# main()
# --------------------------------------------------


if __name__ == "__main__":
    server.listen(5)  # listen to a max of 5 connections
    print("Awaiting new ugo...")
    listenerThread = Thread(target=portListener)
    listenerThread.start()
    listenerThread.join()
    server.close()
