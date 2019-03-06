from loginWidget import*
from ugoChat import*
from registrationPage import *
from registrationPage import Ui_registrationWindow
import sys, sqlite3
from userDatabase import updateTable
from userNotFound import Ui_userNotFoundForm
from loginSuccess import Ui_loginSuccess
from ugoChat import Ui_MainWindow


class myWin(QtWidgets.QMainWindow):#class to create and use objects pertaining to the login screen
    def __init__(self,parent=None):#function to initialize widget
        QtWidgets.QWidget.__init__(self,parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
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

        connection = sqlite3.connect("login.db")
        result = connection.execute("SELECT * FROM USERS WHERE USERNAME = ? AND PASSWORD = ?",(username, password))

        if(len(result.fetchall()) > 0):
            mySuccess.show()#make the object active on the screen
            mySuccess.su.loginSuccessButton.clicked.connect(self.appInitialize)
        else:
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
        global myChat
        myChat = mainChat()
        myChat.show()
        myRegi.close()#will not be needed anymore
        myError.close()#will not be needed anymore
        mySuccess.close()#will not be needed anymore
        myapp.close()#will not be needed anymore


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


if __name__ == "__main__":#Main program execution starts here
    app = QtWidgets.QApplication(sys.argv)
    myapp = myWin()
    myRegi = myReg()
    myError = myErr()
    Rerror = RegError()
    Rsuccess = RegSuccess()
    mySuccess = mySuc()
    myapp.show()
    sys.exit(app.exec_())
