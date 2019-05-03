from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(440, 400)
        font = QtGui.QFont()
        font.setFamily("Monotype Corsiva")


        MainWindow.setFont(font)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.centralwidget.setStyleSheet("background-color: rgb(31, 51, 73);")

        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(0, 0, 141, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.setStyleSheet("background-color: rgb(134, 143, 153);")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.sendMessage_Button = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.sendMessage_Button.setGeometry(QtCore.QRect(410, 310, 31, 31))
        self.sendMessage_Button.setText("")
        self.sendMessage_Button.setObjectName("sendMessage_Button")
        self.sendMessage_LineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.sendMessage_LineEdit.setGeometry(QtCore.QRect(160, 319, 251, 21))


        self.addFriend_LineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.addFriend_LineEdit.setGeometry(QtCore.QRect(0, 319, 99, 21))
        self.addFriend_LineEdit.setObjectName("addFriend_LineEdit")
        self.addFriend_LineEdit.setStyleSheet("background-color: rgb(147, 191, 242);")

        self.addFriend_Button = QtWidgets.QPushButton(self.centralwidget)
        self.addFriend_Button.setGeometry(QtCore.QRect(99, 319, 21, 21))
        self.addFriend_LineEdit.setText("")
        self.addFriend_LineEdit.setPlaceholderText("Add friend here...")
        self.addFriend_Button.setObjectName("addFriend_Button")
        self.addFriend_Button.setIcon(QIcon('addFriend.png'))
        self.addFriend_Button.setStyleSheet("background-color: rgb(74, 116, 138);")

        self.delFriend_Button = QtWidgets.QPushButton(self.centralwidget)
        self.delFriend_Button.setGeometry(QtCore.QRect(120, 319, 21, 21))
        self.delFriend_Button.setObjectName("delFriend_Button")
        self.delFriend_Button.setIcon(QIcon('delFriend.png'))
        self.delFriend_Button.setStyleSheet("background-color: rgb(74, 116, 138);")


        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(85, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 85, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 85, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        self.sendMessage_LineEdit.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.sendMessage_LineEdit.setFont(font)
        self.sendMessage_LineEdit.setAutoFillBackground(False)
        self.sendMessage_LineEdit.setObjectName("sendMessage_LineEdit")
        self.sendMessage_LineEdit.setPlaceholderText("Type here to chat...")

        self.listView = QtWidgets.QListView(self.centralwidget)
        self.listView.setGeometry(QtCore.QRect(0, 20, 141, 300))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(85, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        self.listView.setPalette(palette)
        self.listView.setObjectName("listView")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(160, 0, 281, 320))
        self.textBrowser.setObjectName("textBrowser")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 440, 21))
        self.menubar.setObjectName("menubar")
        self.menuGlobal_Chat = QtWidgets.QMenu(self.menubar)
        self.menuGlobal_Chat.setObjectName("menuGlobal_Chat")

        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionwhat = QtWidgets.QAction(MainWindow)
        self.actionwhat.setObjectName("actionwhat")
        self.menubar.addAction(self.menuGlobal_Chat.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Ugo Chat"))
        MainWindow.setWindowIcon(QtGui.QIcon('bigUgo.png'))
        self.comboBox.setItemText(0, _translate("MainWindow", "Friends"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Settings"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Exit"))
        self.sendMessage_LineEdit.setText(_translate("MainWindow", ""))
        self.addFriend_LineEdit.setText(_translate("MainWindow", ""))
        self.menuGlobal_Chat.setTitle(_translate("MainWindow", "Global Chat"))
        self.actionwhat.setText(_translate("MainWindow", "what"))
