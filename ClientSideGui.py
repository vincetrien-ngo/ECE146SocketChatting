from loginWidget import*
from ugoChat import*
from registrationPage import *
from registrationPage import Ui_registrationWindow
import sys, sqlite3, time, textwrap, os
from userNotFound import Ui_userNotFoundForm
from loginSuccess import Ui_loginSuccess
from ugoChat import Ui_MainWindow
from socket import AF_INET, socket, SOCK_STREAM
from PyQt5.QtCore import QThread, QObject, pyqtSignal, pyqtSlot
from PyQt5.QtGui import *
import datetime


class myWin(QtWidgets.QMainWindow):  # to create and use objects pertaining to the login screen
    def __init__(self, parent=None):  # function to initialize widget
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.REGISTER.clicked.connect(self.openRegistration)
        self.ui.LOGIN.clicked.connect(self.loginCheck)
        self.ui.lineEdit.returnPressed.connect(self.ui.LOGIN.click)

    def openRegistration(self):  # opens registration page and hides login screen
        myRegi.show()  # show registration page
        Rerror.hide()  # If error registering window is displayed then hide it
        myapp.hide()  # hide main login screen
        myRegi.ui.returnButton.clicked.connect(self.returnToLogin)  # event to trigger the login screen
        myRegi.ui.confirmButton.clicked.connect(self.confirmReg)  # event to try logging in
        myRegi.ui.lineEdit_3.returnPressed.connect(myRegi.ui.confirmButton.click)  # When pressing enter initiates the clicking of confirm button

    def confirmReg(self):  # Function to store username and password into server-side database
        inputUser = myRegi.ui.lineEdit.text()  # retrieve text from username textbox
        inputPass = myRegi.ui.lineEdit_2.text()  # retrieve text from password textbox
        confirmPass = myRegi.ui.lineEdit_3.text()  # retrieve text from confirm password textbox

        if inputPass != confirmPass or inputPass == "" or inputUser == "" or confirmPass == "":
            Rerror.show()
            myRegi.ui.lineEdit.clear()  # clear username
            myRegi.ui.lineEdit_2.clear()  # clear password inputs
            myRegi.ui.lineEdit_3.clear()  # clear password inputs
            Rerror.error.userNotFoundButton.clicked.connect(self.openRegistration)
        else:
            send("2")  # invoke command number 2 to prompt the server for registration
            time.sleep(0.3)
            send(inputUser)
            time.sleep(0.3)
            send(inputPass)
            serverResponse = client_socket.recv(BUFSIZ).decode("utf8")

            if serverResponse == "Success":
                Rsuccess.show()
                myRegi.ui.lineEdit.clear()  # clear username input text box
                myRegi.ui.lineEdit_2.clear()  # clear password input text box
                myRegi.ui.lineEdit_3.clear()  # clear confirm password text box
                Rsuccess.success.loginSuccessButton.clicked.connect(self.returnToLogin)
                Rsuccess.success.loginSuccessButton.autoDefault()
            elif serverResponse == "Username Taken!":
                Rerror.show()
                myRegi.ui.lineEdit.clear()  # clear username input text box
                myRegi.ui.lineEdit_2.clear()  # clear password input text box
                myRegi.ui.lineEdit_3.clear()  # clear confirm password text box
                Rerror.error.userNotFoundButton.clicked.connect(self.openRegistration)
            else:
                Rerror.show()
                myRegi.ui.lineEdit.clear()  # clear username input text box
                myRegi.ui.lineEdit_2.clear()  # clear password input text box
                myRegi.ui.lineEdit_3.clear()  # clear confirm password text box
                Rerror.error.userNotFoundButton.clicked.connect(self.openRegistration)

    def loginCheck(self):
        global username
        username = self.ui.UNbox.text()
        password = self.ui.lineEdit.text()

        if not username or not password:
            myError.show()
            self.ui.lineEdit.clear()
            self.ui.UNbox.clear()
            myError.er.userNotFoundButton.clicked.connect(self.returnToLogin)
        else:
            send("1")  # signals a login attempt to the server
            send(username)
            time.sleep(0.2)
            send(password)
            time.sleep(0.2)
            receiveMes = client_socket.recv(BUFSIZ).decode("utf8")

            if receiveMes == "Success":
                friendIndex = 0
                while receiveMes != "FINISHED":  # populate friends list from servers database
                    receiveMes = client_socket.recv(BUFSIZ).decode("utf8")
                    if receiveMes != "FINISHED":
                        userFriends[friendIndex] = receiveMes
                        friendStatus = client_socket.recv(BUFSIZ).decode("utf8")
                        if friendStatus == "ONLINE":
                            userFriendsOnline[friendIndex] = "ONLINE"
                        else:
                            userFriendsOnline[friendIndex] = "OFFLINE"
                        friendIndex += 1

                    time.sleep(0.2)

                mySuccess.show()  # make the object active on the screen
                mySuccess.su.loginSuccessButton.clicked.connect(self.appInitialize)
            else:
                myError.show()
                self.ui.lineEdit.clear()
                self.ui.UNbox.clear()
                myError.er.userNotFoundButton.clicked.connect(self.returnToLogin)

    def returnToLogin(self):  # The back button registration page to go back to login screen
        myapp.show()
        myError.hide()
        Rsuccess.hide()
        myRegi.close()

    def appInitialize(self):  # Start the main chat application after connecting to server
        myChat.show()
        myRegi.close()  # will not be needed anymore
        myError.close()  # will not be needed anymore
        mySuccess.close()  # will not be needed anymore
        myapp.close()  # will not be needed anymore

        self.receiveMessages = receiverThread(username, userFriends, userFriendsOnline)
        self.receiveMessages.start()  # start thread to receive messages in pseudo parallel to running the gui

        myChat.mainChat.addFriend_Button.clicked.connect(self.addingFriend)

        myChat.mainChat.sendMessage_Button.clicked.connect(self.sendMessage)
        myChat.mainChat.sendMessage_LineEdit.returnPressed.connect(myChat.mainChat.sendMessage_Button.click)


    def sendMessage(self):  # Sends message to server and server then displays it in the global chat
        messageToSend = myChat.mainChat.sendMessage_LineEdit.text()
        myChat.mainChat.sendMessage_LineEdit.clear()
        send(messageToSend, None)

    def addingFriend(self):
        newFriend = myChat.mainChat.addFriend_LineEdit.text()
        myChat.mainChat.addFriend_LineEdit.clear()
        if newFriend:
            send("//VERIFY ADD FRIEND:"+newFriend)



def send(msg, event=None):  # event is passed by binders.
        client_socket.send(bytes(msg, "utf8"))  # send the user input to server for handling

# ***********************************************************************************************************************
# Classes to instantiate gui objects##
# ***********************************************************************************************************************
class myReg(QtWidgets.QMainWindow):  # class to create and use objects pertaining to the registration page
    def __init__(self, parent=None):  # function to initialize widget
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_registrationWindow()
        self.ui.setupUi(self)


class myErr(QtWidgets.QMainWindow):  # class used to create error message window for login screen
    def __init__(self, parent=None):  # function to initialize widget
        QtWidgets.QWidget.__init__(self, parent)
        self.er = Ui_userNotFoundForm()
        self.er.setupUi(self)


class RegError(QtWidgets.QMainWindow):
    def __init__(self, parent=None):  # function to initialize widget
        QtWidgets.QWidget.__init__(self, parent)
        self.error = Ui_userNotFoundForm()
        self.error.setupUi(self)
        self.error.userNotFoundLabel.setGeometry(QtCore.QRect(50, 40, 154, 24))
        self.error.userNotFoundLabel.setText("Error Registering!")


class RegSuccess(QtWidgets.QMainWindow):
    def __init__(self, parent=None):  # function to initialize widget
        QtWidgets.QWidget.__init__(self, parent)
        self.success = Ui_loginSuccess()
        self.success.setupUi(self)  # setup the user interface
        self.success.loginSuccessLabel.setGeometry(QtCore.QRect(15,40,215,24))  # set x,y,width,and height parameters for label
        self.success.loginSuccessLabel.setText("Registration Successful!")  # set the text inside the label


class mySuc(QtWidgets.QMainWindow):  # class used to create successful login popup window for login screen
    def __init__(self, parent=None):  # function to initialize widget
        QtWidgets.QWidget.__init__(self, parent)
        self.su = Ui_loginSuccess()
        self.su.setupUi(self)


class mainChat(QtWidgets.QMainWindow):  # class used to create the main chat widget after logging in successfully
    def __init__(self, parent=None):  # function to initialize widget
        QtWidgets.QWidget.__init__(self, parent)
        self.mainChat = Ui_MainWindow()
        self.mainChat.setupUi(self)



    def closeEvent(self, event):
        send("//exit")
        client_socket.close()  # close the socket connection
        myChat.close()
        exit()

# ----------------------------------------------------------------------------------------------------------------------
# Other Functions and threads
# ----------------------------------------------------------------------------------------------------------------------
class receiverThread(QThread):
    def __init__(self, name, friendsOfUser = {}, isOnline = {}, parent=None):
        super(receiverThread, self).__init__(parent)
        self.friendsList = friendsOfUser
        self.friendsOnline = isOnline
        self.yourMes = name

    def run(self):
        synchronizeFriends = friendSync(self.friendsList, self.friendsOnline)
        synchronizeFriends.start()
        msg = "Admin: Treat each other with respect"
        msg.encode("utf8")
        currTime = time.time()
        stringTime = datetime.datetime.fromtimestamp(currTime).strftime('%H:%M:%S __ %m-%d-%Y ---')
        msg = '<p style="background-color: #586e84"><font color="white">%s <br><span>---TimeStamp: %s</span></font></p>' % (msg, stringTime)
        myChat.mainChat.textBrowser.append(msg)
        while True:
            try:
                msg = client_socket.recv(BUFSIZ).decode("utf8")  # receive messages handled by server
                #experimental-------------------------------------
                if "//CANNOT ADD FRIEND" in msg and not msg.find("//CANNOT ADD FRIEND"):
                    print("user does not exit or is already a friend")
                elif "//VERIFY ADD FRIEND:" in msg and not msg.find("//VERIFY ADD FRIEND:"):  # server verifying the addition of a new friend
                    synchronizeFriends.friendToAdd = msg[20:len(msg)-1]
                    if "0" in msg[len(msg)-1:len(msg)]:
                        synchronizeFriends.friendToAddStatus = "OFFLINE"
                    else:
                        synchronizeFriends.friendToAddStatus = "ONLINE"
                    synchronizeFriends.performAdd = True
                elif ":" not in msg:  # update the online status of a friend
                    if msg not in self.yourMes:
                        synchronizeFriends.friendToUpdate = msg
                        synchronizeFriends.performSync = True
                #experimental------------------------------------
                elif not msg.find(self.yourMes+":"):
                    currTime = time.time()
                    stringTime = datetime.datetime.fromtimestamp(currTime).strftime('%H:%M:%S __ %m-%d-%Y ---')
                    msg = '<p style="background-color: #01bdc4">%s <br><span style="background-color:#01bdc4">---TimeStamp: %s</span></p>' % (msg, stringTime)
                    myChat.mainChat.textBrowser.append(msg)  # append to chat box
                else:
                    currTime = time.time()
                    stringTime = datetime.datetime.fromtimestamp(currTime).strftime('%H:%M:%S __ %m-%d-%Y ---')
                    msg = '<p style="background-color: #11ad16">%s <br><span style="background-color:#11ad16">---TimeStamp: %s</span></p>' % (msg, stringTime)
                    myChat.mainChat.textBrowser.append(msg)  # append to chat box
            except OSError:  # catch operating system errors.
                break

class friendSync(QThread):
    def __init__(self, userFriends = [], userFriendsOnline = [], parent=None):
        super(friendSync, self).__init__(parent)
        self.friendsList = userFriends  # list of friends passed into thread
        self.friendsOnline = userFriendsOnline  # list holding status of each friend passed into thread
        self.performSync = False  # status flag to perform a synchronization of list with servers up to date list
        self.performAdd = False  # status flag to perform add friend operation
        self.friendToAdd = ""  # friend that will be added to the list
        self.friendToAddStatus = ""  # online status of friend being added to the list
        self.friendToUpdate = ""  # current friend that has either logged in or out recently
        self.friendship = QStandardItemModel(myChat.mainChat.listView)  # item model to display friends on QlistView

    def run(self):
        for user in self.friendsList:
            if self.friendsOnline[user] == "ONLINE":
                self.friend = QStandardItem(QtGui.QIcon('userOnline.png'), self.friendsList[user])
            else:
                self.friend = QStandardItem(QtGui.QIcon('userOffline.png'), self.friendsList[user])
            self.friendship.appendRow(self.friend)
        myChat.mainChat.listView.setModel(self.friendship)

        while True:
            if self.performSync:
                for friend in self.friendsList:
                    if self.friendsList[friend] == self.friendToUpdate:
                        if self.friendsOnline[friend] == "ONLINE":
                            self.friendsOnline[friend] = "OFFLINE"
                            self.friendship.setItem(friend, QStandardItem(QtGui.QIcon('userOffline.png'), self.friendToUpdate))
                        else:
                            self.friendsOnline[friend] = "ONLINE"
                            self.friendship.setItem(friend, QStandardItem(QtGui.QIcon('userOnline.png'), self.friendToUpdate))
                        self.performSync = False
                        break

            if self.performAdd:
                self.friendsList[len(self.friendsList)+1] = self.friendToAdd
                if "OFFLINE" in self.friendToAddStatus:
                    self.friendship.appendRow(QStandardItem(QtGui.QIcon("userOffline.png"), self.friendToAdd))
                    self.friendsOnline[len(self.friendsOnline)+1] = "OFFLINE"
                else:
                    self.friendship.appendRow(QStandardItem(QtGui.QIcon("userOnline.png"), self.friendToAdd))
                    self.friendsOnline[len(self.friendsOnline)+1] = "ONLINE"
                self.performAdd = False

# ----------------------------------------------------------------------------------------------------------------------
# SOCKET SECTION OF THE PROGRAM TO CONNECT TO SERVER
# ----------------------------------------------------------------------------------------------------------------------
global haveLoggedIn
haveLoggedIn = False
userFriends = {}
userFriendsOnline = {}
host = '73.235.230.212'
#host = '127.0.0.1'
port = 50000
BUFSIZ = 1024
ADDR = (host, port)
client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect(ADDR)

# ----------------------------------------------------------------------------------------------------------------------
# GUI SECTION OF THE PROGRAM TO INITIALIZE DIFFERENT GUI OBJECTS BEFORE HAVING TO DISPLAY THEM LATER IN THE PROGRAM
# ----------------------------------------------------------------------------------------------------------------------
if __name__ == "__main__":  # Main GUI program execution starts here
    app = QtWidgets.QApplication(sys.argv)
    myapp = myWin()
    myRegi = myReg()
    myError = myErr()
    Rerror = RegError()
    Rsuccess = RegSuccess()
    mySuccess = mySuc()
    myChat = mainChat()
    myapp.show()
    sys.exit(app.exec_())

    #  User by Luis Prado from the Noun Project (ugo chat online/ offline icon)
    #  User by Wilson Joseph from the Noun Project(message received icon)
    #  add by Roselin Christina.S from the Noun Project(add friend icon)
