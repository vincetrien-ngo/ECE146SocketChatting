import sqlite3

def createTable():#function to create a new database
    connection = sqlite3.connect("login.db")
    connection.execute("CREATE TABLE USERS(USERNAME TEXT NOT NULL, PASSWORD TEXT)")
    connection.execute("INSERT INTO USERS VALUES(?,?)",('hannsel101','Camacho101'))
    connection.commit()
    result = connection.execute("SELECT * FROM USERS")
    connection.close()

def updateTable(username,password):#function to add users into server database
    userInfo = sqlite3.connect("login.db")
    userInfo.execute("INSERT INTO USERS VALUES(?,?)",(username,password))
    userInfo.commit()
    userInfo.close()

