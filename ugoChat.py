from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(440, 391)
        font = QtGui.QFont()
        font.setFamily("Monotype Corsiva")
        font.setItalic(True)
        MainWindow.setFont(font)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(0, 0, 161, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        #self.comboBox.addItem("")
        self.sendMessage_Button = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.sendMessage_Button.setGeometry(QtCore.QRect(410, 310, 31, 31))
        self.sendMessage_Button.setText("")
        self.sendMessage_Button.setObjectName("sendMessage_Button")
        self.sendMessage_LineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.sendMessage_LineEdit.setGeometry(QtCore.QRect(162, 319, 241, 21))
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
        self.listView = QtWidgets.QListView(self.centralwidget)
        self.listView.setGeometry(QtCore.QRect(0, 20, 161, 321))
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
        self.textBrowser.setGeometry(QtCore.QRect(160, 0, 281, 321))
        self.textBrowser.setObjectName("textBrowser")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 440, 21))
        self.menubar.setObjectName("menubar")
        self.menuGlobal_Chat = QtWidgets.QMenu(self.menubar)
        self.menuGlobal_Chat.setObjectName("menuGlobal_Chat")
        self.menuIndividual = QtWidgets.QMenu(self.menubar)
        self.menuIndividual.setObjectName("menuIndividual")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionwhat = QtWidgets.QAction(MainWindow)
        self.actionwhat.setObjectName("actionwhat")
        self.menubar.addAction(self.menuGlobal_Chat.menuAction())
        self.menubar.addAction(self.menuIndividual.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Ugo Chat"))
        MainWindow.setWindowIcon(QtGui.QIcon('bigUgo.png'))
        #self.comboBox.setItemText(0, _translate("MainWindow", "Menu"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Friends"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Settings"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Exit"))
        self.sendMessage_LineEdit.setText(_translate("MainWindow", "Type here to chat"))
        self.menuGlobal_Chat.setTitle(_translate("MainWindow", "Global Chat"))
        self.menuIndividual.setTitle(_translate("MainWindow", "Individual"))
        self.actionwhat.setText(_translate("MainWindow", "what"))
