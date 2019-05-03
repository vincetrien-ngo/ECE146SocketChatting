import socket, time, signal, sqlite3, sys
from userDatabase import updateTable, checkOnlineStatus, checkAllOnlineStatus, checkFriends
from userDatabase import checkTable, checkUserName, friendsList, updateFriends
from threading import Thread

#--------------------------------------------------
#Initialize the Server
#--------------------------------------------------
clients = {}#stores new clients
addresses = {}#stores new clients addresses
BUFSIZ = 1024#Change this value to change the buffersize of sockets

server = socket.socket()  # server is now socket type and can receive/send through sockets
host = '127.0.0.1'
#host = '192.168.0.44'
port = 50000  # Port to be used for external access to my server
server.bind((host, port))  # Bind the socket type to host/port

#--------------------------------------------------
#Server Functions for listening, sending, handling, and receiving
#--------------------------------------------------
def portListener():#listen for new clients
    while True:
        client, clientAddress = server.accept()#accept the new TCP connection
        print("%s:%s has established a connection." % clientAddress)#Notify server of new connection
        addresses[client] = clientAddress#store clients address in list
        Thread(target=handleClient, args=(client,)).start()#initialize new thread

def handleClient(client):#handle client interaction
    loggedIn = False
    name = ""#user has not logged in yet
    cmdNum = ""
    while not loggedIn:
        while not cmdNum:
            cmdNum = client.recv(BUFSIZ).decode("utf8")

        if cmdNum == "1":#read command number for login attempt
            name = client.recv(BUFSIZ).decode("utf8")#receive the clients name
            time.sleep(0.2)
            passWord = client.recv(BUFSIZ).decode("utf8")#receive the clients password
            if checkTable(name,passWord):
                loggedIn = True
                friendsList(name)  #  check friendsList database exist
                client.send(bytes("Success", "utf8"))
                time.sleep(0.2)

                refreshOnlineFriends(name, client, clients)

            else:
                client.send(bytes("Failed", "utf8"))
                cmdNum = ""
        elif cmdNum == "2":#register attempt
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
    print("%s successfully logged in." % clients[client])
    broadcast(bytes(name, "utf8"))  #  prompt other users to update friends list
    while True:  # loop in charge of allowing the client pass messages
        msg = client.recv(BUFSIZ)  # receive message from client

        if "//VERIFY ADD FRIEND:" in msg.decode("utf8"):  # user is attempting to add a friend           
            if checkUserName(msg[20:len(msg)].decode("utf8")):
                if checkFriends(name, msg[20:len(msg)].decode("utf8")):
                    client.send(bytes("//CANNOT ADD FRIEND", "utf8"))
                else:
                    #updateFriends(name, msg[20:len(msg)].decode("utf8"))
                    updateFriends(name, msg[20:len(msg)].decode("utf8"), "ADD FRIEND")
                    onlineFlag = False
                    for people in clients:
                        if msg[20:len(msg)].decode("utf8") == clients[people]:
                            onlineFlag = True
                    if onlineFlag:
                        client.send(msg + bytes("1", "utf8"))
                    else:
                        client.send(msg + bytes("0", "utf8"))
            else:
                client.send(bytes("//CANNOT ADD FRIEND", "utf8"))
        elif "//VERIFY DEL FRIEND:" in msg.decode("utf8"):  # user is attempting to delete friend
            if checkUserName(msg[20:len(msg)].decode("utf8")):
                if checkFriends(name, msg[20:len(msg)].decode("utf8")):
                    updateFriends(name, msg[20:len(msg)].decode("utf8"), "DELETE")
                    client.send(msg)
                else:
                    client.send(bytes("//CANNOT DEL FRIEND:", "utf8"))
            else:
                client.send(bytes("//CANNOT DEL FRIEND:", "utf8"))
        elif msg != bytes("//exit", "utf8"):
            broadcast(msg, name+": ")  # Send message to all other users
        else:  # user wishes to disconnect
            print("%s has disconnected." % clients[client])
            client.close()  # remove clients socket connection
            del clients[client]  # delete client from list of clients
            broadcast(bytes(name, "utf8"))  #  signal users to update online friends
            broadcast(bytes("SERVER: %s has disconnected from Ugo Chat." % name, "utf8"))  # broadcast exit
            break  # end of while loop


def broadcast(msg, prefix=""):  # handles the broadcasting of messages to all users
    for sock in clients:  # iterate through all clients receiving socket
        sock.send(bytes(prefix, "utf8")+msg)  # send the msg to each client

def refreshOnlineFriends(name, client, clients = []):
    checkAllOnlineStatus(name, clients) #  check if friends are logged in

    connection = sqlite3.connect(name + ".db")
    results = connection.cursor()

    currFriends = results.execute("SELECT * FROM friends").fetchall()
    currResult = 0
    if currFriends:
        for result in currFriends:
            client.send(bytes(currFriends[currResult][0], "utf8"))
            time.sleep(0.3)
            if currFriends[currResult][1] == 1:
                client.send(bytes("ONLINE", "utf8"))
            else:
                client.send(bytes("OFFLINE", "utf8"))
            currResult = currResult + 1
            time.sleep(0.3)
    connection.close()
    client.send(bytes("FINISHED", "utf8"))
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
