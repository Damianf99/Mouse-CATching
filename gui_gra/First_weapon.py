from PyQt5 import QtCore, QtGui, QtWidgets
import pygame
import os
import time
import random

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        """
        Główna klasa gui pierwszej broni do wyboru
        """
        MainWindow.setObjectName("Mouse CATching")
        MainWindow.resize(450, 450)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.photo = QtWidgets.QLabel(self.centralwidget)
        self.photo.setGeometry(QtCore.QRect(6, 2, 450, 450))
        self.photo.setText("")
        self.photo.setPixmap(QtGui.QPixmap("assets/tlo.png"))
        self.photo.setObjectName("photo")
        self.Choose_Label = QtWidgets.QLabel(self.centralwidget)
        self.Choose_Label.setGeometry(QtCore.QRect(75, 130, 301, 71))
        font = QtGui.QFont()
        font.setFamily("Courier")
        font.setBold(True)
        font.setPointSize(16)
        self.Choose_Label.setFont(font)
        self.Choose_Label.setObjectName("Choose_Label")
        self.Blue_Blast_Button = QtWidgets.QPushButton(self.centralwidget)
        self.Blue_Blast_Button.setGeometry(QtCore.QRect(50, 220, 81, 51))
        self.Blue_Blast_Button.setStyleSheet("")
        self.Blue_Blast_Button.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("assets/Blue_Blast.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Blue_Blast_Button.setIcon(icon)
        self.Blue_Blast_Button.setIconSize(QtCore.QSize(100, 90))
        self.Blue_Blast_Button.setFlat(False)
        self.Blue_Blast_Button.setObjectName("Blue_Blast_Button")
        self.Light_Blast_Button = QtWidgets.QPushButton(self.centralwidget)
        self.Light_Blast_Button.setGeometry(QtCore.QRect(180, 220, 81, 51))
        self.Light_Blast_Button.setStyleSheet("")
        self.Light_Blast_Button.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("assets/Light_Blast.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Light_Blast_Button.setIcon(icon1)
        self.Light_Blast_Button.setIconSize(QtCore.QSize(100, 90))
        self.Light_Blast_Button.setObjectName("Light_Blast_Button")
        self.Red_Blast_Button = QtWidgets.QPushButton(self.centralwidget)
        self.Red_Blast_Button.setGeometry(QtCore.QRect(310, 220, 81, 51))
        self.Red_Blast_Button.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("assets/Red_Blast.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Red_Blast_Button.setIcon(icon2)
        self.Red_Blast_Button.setIconSize(QtCore.QSize(100, 90))
        self.Red_Blast_Button.setObjectName("Red_Blast_Button")
        self.Blue_Blast_Label = QtWidgets.QLabel(self.centralwidget)
        self.Blue_Blast_Label.setGeometry(QtCore.QRect(55, 275, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Blue_Blast_Label.setFont(font)
        self.Blue_Blast_Label.setObjectName("Blue_Blast_Label")
        self.Light_Blast_Label = QtWidgets.QLabel(self.centralwidget)
        self.Light_Blast_Label.setGeometry(QtCore.QRect(185, 275, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Light_Blast_Label.setFont(font)
        self.Light_Blast_Label.setObjectName("Light_Blast_Label")
        self.Red_Blast_Label = QtWidgets.QLabel(self.centralwidget)
        self.Red_Blast_Label.setGeometry(QtCore.QRect(315, 275, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Red_Blast_Label.setFont(font)
        self.Red_Blast_Label.setObjectName("Red_Blast_Label")
        self.Start = QtWidgets.QPushButton(self.centralwidget)
        self.Start.setGeometry(QtCore.QRect(180, 320, 100, 31))
        self.Start.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("assets/start.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Start.setIcon(icon3)
        self.Start.setIconSize(QtCore.QSize(100, 90))
        self.Start.setFlat(True)
        self.Start.setObjectName("Start")
        self.photo.raise_()
        self.Choose_Label.raise_()
        self.Light_Blast_Button.raise_()
        self.Red_Blast_Button.raise_()
        self.Blue_Blast_Button.raise_()
        self.Blue_Blast_Label.raise_()
        self.Light_Blast_Label.raise_()
        self.Red_Blast_Label.raise_()
        self.Start.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 450, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.Start.clicked.connect(self.start)
        self.Blue_Blast_Button.clicked.connect(self.BlueBlast)
        self.Light_Blast_Button.clicked.connect(self.LightBlast)
        self.Red_Blast_Button.clicked.connect(self.RedBlast)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Choose_Label.setText(_translate("MainWindow", "Choose your first weapon!"))
        self.Blue_Blast_Label.setText(_translate("MainWindow", "Blue Blast"))
        self.Light_Blast_Label.setText(_translate("MainWindow", "Light Blast"))
        self.Red_Blast_Label.setText(_translate("MainWindow", "Red Blast"))

    def start(self):
        """
        Funkcja zamykająca okno gui
        """
        MainWindow.close()

    def BlueBlast(self):
        """
        Funkcja odpowiedzialna za ustawienie broni oraz przestawienie atrybutów gracza
        """
        player_gui.laser_img = pygame.image.load(os.path.join("assets", "Blue_Blast.png"))
        player_gui.attack = 10

    def LightBlast(self):
        """
        Funkcja odpowiedzialna za ustawienie broni oraz przestawienie atrybutów gracza
        """
        player_gui.laser_img = pygame.image.load(os.path.join("assets", "Light_Blast.png"))
        player_gui.attack = 10

    def RedBlast(self):
        """
        Funkcja odpowiedzialna za ustawienie broni oraz przestawienie atrybutów gracza
        """
        player_gui.laser_img = pygame.image.load(os.path.join("assets", "Red_Blast.png"))
        player_gui.attack = 10

def change_player(player):
    """
    Funkcja odpowiedzialna za otworzenie gui wyboru pierwszej broni
    """
    import sys
    global app
    app = QtWidgets.QApplication(sys.argv)
    global MainWindow
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    global player_gui
    player_gui = player
    app.exec_()
