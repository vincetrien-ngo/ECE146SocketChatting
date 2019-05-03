import sqlite3

def createTable():#function to create a new database
    connection = sqlite3.connect("login.db")
    connection.execute("CREATE TABLE USERS(USERNAME TEXT NOT NULL, PASSWORD TEXT)")
    connection.commit()
    connection.close()

def friendsList(username):#function to create a friends list for every unique user
    connection = sqlite3.connect(username + ".db")  #If file exist connect to it, else create it
    connection.execute("CREATE TABLE IF NOT EXISTS friends(friend TEXT NOT NULL PRIMARY KEY, online INTEGER)")  #Create friendslist table if it does not exist
    connection.commit()
    connection.close()

#def updateFriends(username, newFriend):#update a users friends list
def updateFriends(username, newFriend, action):#update a users friends list
    connection = sqlite3.connect(username + ".db")  #connect to database file
    checkFriends = connection.execute("SELECT friend FROM friends WHERE friend = ?",(newFriend,))
    if(checkFriends.fetchone()):
        if "DELETE" in action:
            connection.execute("DELETE FROM friends WHERE friend = ?", (newFriend,))
            connection.commit()
        connection.close()
    else:
        connection.execute("INSERT INTO friends VALUES(?,?)",(newFriend, 0))
        connection.commit()
        connection.close()

def checkOnlineStatus(username, client, statusUpdate):  #  user is the current user and client is another user that is logged in
    connection = sqlite3.connect(username + ".db")
    checkFriends = connection.execute ("SELECT friend FROM friends WHERE friend = ?", (client,))
    if checkFriends.fetchone():
        connection.execute("UPDATE friends SET online = ?  WHERE friend = ?", (statusUpdate, client))
        connection.commit()
        connection.close()
    else:
        connection.close()

def checkAllOnlineStatus(username, clients = []):  #  similar to checkOnlineStatus() but checks all friends instead of just one
    connection = sqlite3.connect(username + ".db")
    checkFriends = connection.execute("SELECT friend FROM friends")  #  retreive full list of friends
    for currIndex in checkFriends:
        if currIndex in clients:
            connection.execute("UPDATE friends SET online = ? WHERE friend = ?", (1, currIndex[0]))
            connection.commit()
        else:
            connection.execute("UPDATE friends SET online = ? WHERE friend = ?", (0, currIndex[0]))
            connection.commit()

    connection.close()

def checkFriends(username, newFriend):
    userInfo = sqlite3.connect(username + ".db")
    result = userInfo.execute("SELECT * FROM friends WHERE friend = ?",(newFriend,))
    if(len(result.fetchall()) > 0):
        return True
    else:
        return False
        
def updateTable(username,password):#function to add users into server database
    userInfo = sqlite3.connect("login.db")
    userInfo.execute("INSERT INTO USERS VALUES(?,?)",(username,password))
    userInfo.commit()
    userInfo.close()

def checkTable(username, password):
    userInfo = sqlite3.connect("login.db")
    result = userInfo.execute("SELECT * FROM USERS WHERE USERNAME = ? AND PASSWORD = ?",(username, password))
    if(len(result.fetchall()) > 0):
        return True
    else:
        return False

def checkUserName(username):
    userInfo = sqlite3.connect("login.db")
    result = userInfo.execute("SELECT * FROM USERS WHERE USERNAME = ?", (username,))
    if(len(result.fetchall()) > 0):
        return True
    else:
        return False

