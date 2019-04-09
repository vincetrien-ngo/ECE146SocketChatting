import sqlite3

def createTable():#function to create a new database
    connection = sqlite3.connect("login.db")
    connection.execute("CREATE TABLE USERS(USERNAME TEXT NOT NULL, PASSWORD TEXT)")
    connection.commit()
    result = connection.execute("SELECT * FROM USERS")
    connection.close()
#################EXPERIMENTAL FUNCTION##################################################
def friendsList(username):#function to create a friends list for every unique user
    connection = sqlite3.connect(username + ".db")  #If file exist connect to it, else create it
    connection.execute("CREATE TABLE IF NOT EXISTS friends(friend TEXT NOT NULL PRIMARY KEY, online INTEGER)")  #Create friendslist table if it does not exist
    connection.commit()
    connection.close()

def updateFriends(username, newFriend):#update a users friends list
    connection = sqlite3.connect(username + ".db")  #connect to database file
    checkFriends = connection.execute("SELECT friend FROM friends WHERE friend = ?",(newFriend))
    if(checkFriends.fetchone()):
        connection.close()
    else:
        connection.execute("INSERT INTO friends VALUES(?,?)",(newFriend, 0))
        connection.commit()
        connection.close()
     
#################EXPERIMENTAL FUNCTION##################################################
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

