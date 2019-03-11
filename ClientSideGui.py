from loginWidget import*
from ugoChat import*
from registrationPage import *
from registrationPage import Ui_registrationWindow
import sys, sqlite3, time
from userNotFound import Ui_userNotFoundForm
from loginSuccess import Ui_loginSuccess
from ugoChat import Ui_MainWindow
from socket import AF_INET, socket, SOCK_STREAM
from PyQt5.QtCore import QThread, QObject, pyqtSignal, pyqtSlot


class myWin(QtWidgets.QMainWindow):#class to create and use objects pertaining to the login screen
    def __init__(self,parent=None):#function to initialize widget
        QtWidgets.QWidget.__init__(self,parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        """self.workerThread = WorkerThread()
        self.workerThread.start()
        self.sendThread = senderThread()
        self.sendThread.start()"""
        print('prelogin button pressed')
        self.ui.REGISTER.clicked.connect(self.openRegistration)
        self.ui.LOGIN.clicked.connect(self.loginCheck)


    def openRegistration(self):#opens registration page and hides login screen
        myRegi.show()#show registration page
        Rerror.hide()#If error registering window is displayed then hide it
        myapp.hide()#hide main login screen
        myRegi.ui.returnButton.clicked.connect(self.returnToLogin)#event to trigger the login screen
        myRegi.ui.confirmButton.clicked.connect(self.confirmReg)#event to try logging in

    def confirmReg(self):#Function to store username and password into serverside database
        inputUser = myRegi.ui.lineEdit.text()#retrieve text from username textbox
        inputPass = myRegi.ui.lineEdit_2.text()#retrieve text from password textbox
        confirmPass = myRegi.ui.lineEdit_3.text()#retrive text from confirm password textbox

        if(inputPass != confirmPass):
            Rerror.show()
            myRegi.ui.lineEdit_2.clear()#clear password inputs
            myRegi.ui.lineEdit_3.clear()#clear password inputs
            Rerror.error.userNotFoundButton.clicked.connect(self.openRegistration)
        else:
            Rsuccess.show()
            updateTable(inputUser,inputPass)#add user to database
            myRegi.ui.lineEdit.clear()#clear username input text box
            myRegi.ui.lineEdit_2.clear()#clear password input text box
            myRegi.ui.lineEdit_3.clear()#clear confirm password text box
            Rsuccess.success.loginSuccessButton.clicked.connect(self.returnToLogin)

    def loginCheck(self):
        username = self.ui.UNbox.text()
        password = self.ui.lineEdit.text()
        send("1")#signals a login attempt to the server
        send(username)
        time.sleep(1)
        send(password)
        time.sleep(1)
        receiveMes = client_socket.recv(BUFSIZ).decode("utf8")

        if receiveMes == "Success":
            print('reached here success')
            mySuccess.show()#make the object active on the screen
            mySuccess.su.loginSuccessButton.clicked.connect(self.appInitialize)
        else:
            print('reached here error')
            myError.show()
            self.ui.lineEdit.clear()
            self.ui.UNbox.clear()
            myError.er.userNotFoundButton.clicked.connect(self.returnToLogin)


    def returnToLogin(self):#The back button registration page to go back to login screen
        myapp.show()
        myError.hide()
        Rsuccess.hide()
        myRegi.close()

    def appInitialize(self):#Start the main chat application after connecting to server
        myChat.show()
        myRegi.close()#will not be needed anymore
        myError.close()#will not be needed anymore
        mySuccess.close()#will not be needed anymore
        myapp.close()#will not be needed anymore

        myChat.mainChat.sendMessage_Button.clicked.connect(self.sendMessage)

    def sendMessage(self):#Sends message to server and server then displays it in the global chat
        messageToSend = myChat.mainChat.sendMessage_LineEdit.text()
        myChat.mainChat.textBrowser.append(messageToSend)
        send(messageToSend,None)

def send(msg, event=None):  # event is passed by binders.
    client_socket.send(bytes(msg, "utf8"))#send the user input to server for handling
    if msg == "{exit}":#typing {exit} will cause client to exit
        client_socket.close()#close the socket connection

def receive():
    if haveLoggedIn:
        while True:
            try:
                msg = client_socket.recv(BUFSIZ).decode("utf8")#recieve messages handled by server
                myChat.mainChat.textBrowser.append(msg)
            except OSError:  # Possibly client has left the chat.
                break
    else:
        print('im here')
        while not haveLoggedIn:
            username = myapp.ui.UNbox.text()
            password = myapp.ui.lineEdit.text()
            send(username)
            send(password)
            if client_socket.recv(BUFSIZ).decode("utf8") == "Success":
                haveLoggedIn = True
                receive()


#***********************************************************************************************************************
##Classes to instantiate gui objects##
#***********************************************************************************************************************

class myReg(QtWidgets.QMainWindow):#class to create and use objects pertaining to the registration page
    def __init__(self, parent=None):#function to initialize widget
        QtWidgets.QWidget.__init__(self,parent)
        self.ui = Ui_registrationWindow()
        self.ui.setupUi(self)

class myErr(QtWidgets.QMainWindow):#class used to create error message window for login screen
    def __init__(self, parent=None):#function to initialize widget
        QtWidgets.QWidget.__init__(self,parent)
        self.er = Ui_userNotFoundForm()
        self.er.setupUi(self)

class RegError(QtWidgets.QMainWindow):
    def __init__(self, parent=None):#function to initialize widget
        QtWidgets.QWidget.__init__(self,parent)
        self.error = Ui_userNotFoundForm()
        self.error.setupUi(self)
        self.error.userNotFoundLabel.setGeometry(QtCore.QRect(50, 40, 154, 24))
        self.error.userNotFoundLabel.setText("Error Registering!")

class RegSuccess(QtWidgets.QMainWindow):
    def __init__(self,parent=None):#function to initialize widget
        QtWidgets.QWidget.__init__(self,parent)
        self.success = Ui_loginSuccess()
        self.success.setupUi(self)#setup the user interface
        self.success.loginSuccessLabel.setGeometry(QtCore.QRect(15,40,215,24))#set x,y,width,and height parameters for label
        self.success.loginSuccessLabel.setText("Registration Successful!")#set the text inside the label

class mySuc(QtWidgets.QMainWindow):#class used to create successful login popup window for login screen
    def __init__(self, parent=None):#function to initialize widget
        QtWidgets.QWidget.__init__(self,parent)
        self.su = Ui_loginSuccess()
        self.su.setupUi(self)

class mainChat(QtWidgets.QMainWindow):#class used to create the main chat widget after logging in successfully
    def __init__(self, parent=None):#function to initialize widget
        QtWidgets.QWidget.__init__(self,parent)
        self.mainChat = Ui_MainWindow()
        self.mainChat.setupUi(self)

class WorkerThread(QThread):
    def __init__(self, parent=None):
        super(WorkerThread,self).__init__(parent)

    def run(self):
        while True:
            print("this is running still")
            time.sleep(2)

class senderThread(QThread):
    def __init__(self, parent=None):
        super(senderThread,self).__init__(parent)

    def run(self):
        while True:
            print("this happens also")
            time.sleep(0.5)
##----------------------------------------------------------------------------------------------------------------------
##SOCKET SECTION OF THE PROGRAM TO CONNECT TO SERVER AND CREATE THREADS
##----------------------------------------------------------------------------------------------------------------------
def on_closing(event=None):
    my_msg.set("{exit}")
    send()

##----------------------------------------------------------------------------------------------------------------------
##GUI SECTION OF THE PROGRAM TO INITIALIZE DIFFERENT GUI OBJECTS BEFORE HAVING TO DISPLAY THEM LATER IN THE PROGRAM
##----------------------------------------------------------------------------------------------------------------------
global haveLoggedIn
haveLoggedIn = False
#host = '192.168.0.44'
host = '73.235.230.212'
port = 50000
BUFSIZ = 1024
ADDR = (host, port)
client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect(ADDR)


if __name__ == "__main__":#Main program execution starts here
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
