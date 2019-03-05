from loginWidget import*
from ugoChat import*
from registrationPage import *
from registrationPage import Ui_registrationWindow
import sys, sqlite3
from userDatabase import updateTable


class myWin(QtWidgets.QMainWindow):#class to create and use objects pertaining to the login screen
    def __init__(self,parent=None):
        QtWidgets.QWidget.__init__(self,parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.REGISTER.clicked.connect(self.openRegistration)
        self.ui.LOGIN.clicked.connect(self.loginCheck)

    def openRegistration(self):#opens registration page and hides login screen
        myRegi.show()
        myapp.hide()
        myRegi.ui.returnButton.clicked.connect(self.returnToLogin)
        myRegi.ui.confirmButton.clicked.connect(self.confirmReg)

    def confirmReg(self):#Function to store username and password into serverside database
        inputUser = myRegi.ui.lineEdit.text()
        inputPass = myRegi.ui.lineEdit_2.text()
        confirmPass = myRegi.ui.lineEdit_3.text()

        if(inputPass != confirmPass):
            print("Passwords do not match")
        else:
            updateTable(inputUser,inputPass)#add user to database

    def loginCheck(self):
        username = self.ui.UNbox.text()
        password = self.ui.lineEdit.text()

        connection = sqlite3.connect("login.db")
        result = connection.execute("SELECT * FROM USERS WHERE USERNAME = ? AND PASSWORD = ?",(username, password))

        if(len(result.fetchall()) > 0):
            print("User Found!")
        else:
            print("User Not Found!")


    def returnToLogin(self):#The back button registration page to go back to login screen
        myRegi.close()
        myapp.show()

class myReg(QtWidgets.QMainWindow):#class to create and use objects pertaining to the registration page
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self,parent)
        self.ui = Ui_registrationWindow()
        self.ui.setupUi(self)



if __name__ == "__main__":#Main program execution starts here
    app = QtWidgets.QApplication(sys.argv)
    myapp = myWin()
    myRegi = myReg()
    myapp.show()
    sys.exit(app.exec_())
