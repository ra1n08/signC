# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\main.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(780, 234)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.CPbtn = QtWidgets.QPushButton(self.centralwidget)
        self.CPbtn.setGeometry(QtCore.QRect(10, 10, 241, 101))
        self.CPbtn.setObjectName("CPbtn")
        self.signbtn = QtWidgets.QPushButton(self.centralwidget)
        self.signbtn.setGeometry(QtCore.QRect(270, 10, 241, 51))
        self.signbtn.setObjectName("signbtn")
        self.unSignbtn = QtWidgets.QPushButton(self.centralwidget)
        self.unSignbtn.setGeometry(QtCore.QRect(530, 10, 241, 51))
        self.unSignbtn.setObjectName("unSignbtn")
        self.pbar = QtWidgets.QProgressBar(self.centralwidget)
        self.pbar.setGeometry(QtCore.QRect(20, 140, 751, 31))
        self.pbar.setProperty("value", 24)
        self.pbar.setObjectName("pbar")
        self.signPathBtn = QtWidgets.QToolButton(self.centralwidget)
        self.signPathBtn.setGeometry(QtCore.QRect(270, 80, 41, 31))
        self.signPathBtn.setObjectName("signPathBtn")
        self.SignPath = QtWidgets.QLineEdit(self.centralwidget)
        self.SignPath.setGeometry(QtCore.QRect(320, 80, 191, 31))
        self.SignPath.setObjectName("SignPath")
        self.UnSignPath = QtWidgets.QLineEdit(self.centralwidget)
        self.UnSignPath.setGeometry(QtCore.QRect(580, 80, 191, 31))
        self.UnSignPath.setObjectName("UnSignPath")
        self.unSignPathbtn = QtWidgets.QToolButton(self.centralwidget)
        self.unSignPathbtn.setGeometry(QtCore.QRect(530, 80, 41, 31))
        self.unSignPathbtn.setObjectName("unSignPathbtn")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 780, 26))
        self.menubar.setObjectName("menubar")
        self.menuMore = QtWidgets.QMenu(self.menubar)
        self.menuMore.setObjectName("menuMore")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionInfo = QtWidgets.QAction(MainWindow)
        self.actionInfo.setObjectName("actionInfo")
        self.actionDebug = QtWidgets.QAction(MainWindow)
        self.actionDebug.setObjectName("actionDebug")
        self.menuMore.addAction(self.actionInfo)
        self.menuMore.addAction(self.actionDebug)
        self.menubar.addAction(self.menuMore.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.CPbtn.setText(_translate("MainWindow", "Create Parameters"))
        self.signbtn.setText(_translate("MainWindow", "Sign"))
        self.unSignbtn.setText(_translate("MainWindow", "Un-Sign"))
        self.signPathBtn.setText(_translate("MainWindow", "..."))
        self.unSignPathbtn.setText(_translate("MainWindow", "..."))
        self.menuMore.setTitle(_translate("MainWindow", "More"))
        self.actionInfo.setText(_translate("MainWindow", "Info"))
        self.actionDebug.setText(_translate("MainWindow", "Debug"))