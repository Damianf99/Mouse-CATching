from PyQt5 import QtCore, QtGui, QtWidgets
import pygame
import os
import time
import random
import sys

class Ui_MainWindow(object):
    def __init__(self,run):
        """
        Główna klasa pierwszego gui do rozpoczęcia gry
        """
        self.run = run
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Mouse CATching")
        MainWindow.resize(450, 450)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Start = QtWidgets.QPushButton(self.centralwidget)
        self.Start.setGeometry(QtCore.QRect(180, 270, 95, 31))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("assets/start.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Start.setIcon(icon)
        self.Start.setIconSize(QtCore.QSize(100, 90))
        self.Start.setFlat(True)
        self.Start.setObjectName("Start")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 450, 450))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("assets/tlo_gui.png"))
        self.label.setObjectName("label")
        self.End = QtWidgets.QPushButton(self.centralwidget)
        self.End.setGeometry(QtCore.QRect(190, 300, 67, 31))
        self.End.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("assets/end.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.End.setIcon(icon1)
        self.End.setIconSize(QtCore.QSize(100, 90))
        self.End.setFlat(True)
        self.End.setObjectName("End")
        self.label.raise_()
        self.Start.raise_()
        self.End.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 450, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.Start.clicked.connect(self.start)
        self.End.clicked.connect(self.stop)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

    def start(self):
        """
        Funkcja zamykająca okno gui i rozpoczynająca grę
        """
        MainWindow.close()

    def stop(self):
        """
        Funkcja zamykająca gui oraz cały program
        """
        MainWindow.close()
        self.run[0] = False

def run_gui(run):
    """
    Funkcja uruchamiająca gui
    """
    global app
    app = QtWidgets.QApplication(sys.argv)
    global MainWindow
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow(run)
    ui.setupUi(MainWindow)
    MainWindow.show()
    app.exec_()
