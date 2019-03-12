import sqlite3

def createTable():#function to create a new database
    connection = sqlite3.connect("login.db")
    connection.execute("CREATE TABLE USERS(USERNAME TEXT NOT NULL, PASSWORD TEXT)")
    connection.commit()
    result = connection.execute("SELECT * FROM USERS")
    connection.close()

def updateTable(username,password):#function to add users into server database
    userInfo = sqlite3.connect("login.db")
    userInfo.execute("INSERT INTO USERS VALUES(?,?)",(username,password))
    userInfo.commit()
    userInfo.close()

def checkTable(username,password):#function to verify user is registered in the server
    userInfo = sqlite3.connect("login.db")
    result = connection.execute("SELECT * FROM USERS WHERE USERNAME = ? AND PASSWORD = ?",(username, password))

    if(len(result.fetchall()) > 0):
        return True
    else:
        return False
