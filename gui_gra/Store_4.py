from PyQt5 import QtCore, QtGui, QtWidgets
import pygame
import os
import time
import random
import sys


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        """
        Główna klasa gui od sklepu w grze
        """
        MainWindow.setObjectName("Mouse CATching")
        MainWindow.resize(450, 450)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 450, 450))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("assets/tlo.png"))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(170, 0, 100, 90))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_2.setFont(font)
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("assets/Store_text.png"))
        self.label_2.setObjectName("label_2")
        self.label_11000 = QtWidgets.QLabel(self.centralwidget)
        self.label_11000.setGeometry(QtCore.QRect(20, 80, 47, 13))
        font = QtGui.QFont()
        font.setFamily("Courier")
        self.label_11000.setFont(font)
        self.label_11000.setObjectName("label_11000")
        self.label_10000 = QtWidgets.QLabel(self.centralwidget)
        self.label_10000.setGeometry(QtCore.QRect(20, 110, 47, 13))
        font = QtGui.QFont()
        font.setFamily("Courier")
        self.label_10000.setFont(font)
        self.label_10000.setObjectName("label_10000")
        self.label_9000 = QtWidgets.QLabel(self.centralwidget)
        self.label_9000.setGeometry(QtCore.QRect(20, 140, 47, 13))
        font = QtGui.QFont()
        font.setFamily("Courier")
        self.label_9000.setFont(font)
        self.label_9000.setObjectName("label_9000")
        self.label_8000 = QtWidgets.QLabel(self.centralwidget)
        self.label_8000.setGeometry(QtCore.QRect(20, 170, 47, 13))
        font = QtGui.QFont()
        font.setFamily("Courier")
        self.label_8000.setFont(font)
        self.label_8000.setObjectName("label_8000")
        self.label_7000 = QtWidgets.QLabel(self.centralwidget)
        self.label_7000.setGeometry(QtCore.QRect(20, 200, 47, 13))
        font = QtGui.QFont()
        font.setFamily("Courier")
        self.label_7000.setFont(font)
        self.label_7000.setObjectName("label_7000")
        self.label_6000 = QtWidgets.QLabel(self.centralwidget)
        self.label_6000.setGeometry(QtCore.QRect(20, 230, 47, 13))
        font = QtGui.QFont()
        font.setFamily("Courier")
        self.label_6000.setFont(font)
        self.label_6000.setObjectName("label_6000")
        self.label_5000 = QtWidgets.QLabel(self.centralwidget)
        self.label_5000.setGeometry(QtCore.QRect(20, 260, 47, 13))
        font = QtGui.QFont()
        font.setFamily("Courier")
        self.label_5000.setFont(font)
        self.label_5000.setObjectName("label_5000")
        self.label_4000 = QtWidgets.QLabel(self.centralwidget)
        self.label_4000.setGeometry(QtCore.QRect(20, 290, 47, 13))
        font = QtGui.QFont()
        font.setFamily("Courier")
        self.label_4000.setFont(font)
        self.label_4000.setObjectName("label_4000")
        self.label_3000 = QtWidgets.QLabel(self.centralwidget)
        self.label_3000.setGeometry(QtCore.QRect(20, 320, 47, 13))
        font = QtGui.QFont()
        font.setFamily("Courier")
        self.label_3000.setFont(font)
        self.label_3000.setObjectName("label_3000")
        self.label_2000 = QtWidgets.QLabel(self.centralwidget)
        self.label_2000.setGeometry(QtCore.QRect(20, 350, 47, 13))
        font = QtGui.QFont()
        font.setFamily("Courier")
        self.label_2000.setFont(font)
        self.label_2000.setObjectName("label_2000")
        self.label_1000 = QtWidgets.QLabel(self.centralwidget)
        self.label_1000.setGeometry(QtCore.QRect(20, 380, 47, 13))
        font = QtGui.QFont()
        font.setFamily("Courier")
        self.label_1000.setFont(font)
        self.label_1000.setObjectName("label_1000")
        self.label_12000 = QtWidgets.QLabel(self.centralwidget)
        self.label_12000.setGeometry(QtCore.QRect(20, 50, 47, 13))
        font = QtGui.QFont()
        font.setFamily("Courier")
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.label_12000.setFont(font)
        self.label_12000.setObjectName("label_12000")
        self.label_Mistic_Violet_Ball = QtWidgets.QLabel(self.centralwidget)
        self.label_Mistic_Violet_Ball.setGeometry(QtCore.QRect(110, 47, 151, 21))
        font = QtGui.QFont()
        font.setFamily("Courier")
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_Mistic_Violet_Ball.setFont(font)
        self.label_Mistic_Violet_Ball.setObjectName("label_Mistic_Violet_Ball")
        self.label_Mistic_Ball = QtWidgets.QLabel(self.centralwidget)
        self.label_Mistic_Ball.setGeometry(QtCore.QRect(110, 80, 121, 16))
        font = QtGui.QFont()
        font.setFamily("Courier")
        font.setBold(True)
        font.setWeight(75)
        self.label_Mistic_Ball.setFont(font)
        self.label_Mistic_Ball.setObjectName("label_Mistic_Ball")
        self.label_Extra_Life = QtWidgets.QLabel(self.centralwidget)
        self.label_Extra_Life.setGeometry(QtCore.QRect(110, 107, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Courier")
        font.setBold(True)
        font.setWeight(75)
        self.label_Extra_Life.setFont(font)
        self.label_Extra_Life.setObjectName("label_Extra_Life")
        self.label_Magic_Snowball = QtWidgets.QLabel(self.centralwidget)
        self.label_Magic_Snowball.setGeometry(QtCore.QRect(110, 137, 121, 21))
        font = QtGui.QFont()
        font.setFamily("Courier")
        font.setBold(True)
        font.setWeight(75)
        self.label_Magic_Snowball.setFont(font)
        self.label_Magic_Snowball.setObjectName("label_Magic_Snowball")
        self.label_Extra_Speed = QtWidgets.QLabel(self.centralwidget)
        self.label_Extra_Speed.setGeometry(QtCore.QRect(110, 167, 101, 21))
        font = QtGui.QFont()
        font.setFamily("Courier")
        font.setBold(True)
        font.setWeight(75)
        self.label_Extra_Speed.setFont(font)
        self.label_Extra_Speed.setObjectName("label_Extra_Speed")
        self.label_Falcon_Blue_Eye = QtWidgets.QLabel(self.centralwidget)
        self.label_Falcon_Blue_Eye.setGeometry(QtCore.QRect(110, 200, 121, 16))
        font = QtGui.QFont()
        font.setFamily("Courier")
        font.setBold(True)
        font.setWeight(75)
        self.label_Falcon_Blue_Eye.setFont(font)
        self.label_Falcon_Blue_Eye.setObjectName("label_Falcon_Blue_Eye")
        self.label_Elite_Sayian_Ball = QtWidgets.QLabel(self.centralwidget)
        self.label_Elite_Sayian_Ball.setGeometry(QtCore.QRect(110, 227, 141, 21))
        font = QtGui.QFont()
        font.setFamily("Courier")
        font.setBold(True)
        font.setWeight(75)
        self.label_Elite_Sayian_Ball.setFont(font)
        self.label_Elite_Sayian_Ball.setObjectName("label_Elite_Sayian_Ball")
        self.label_Eye_of_Nature = QtWidgets.QLabel(self.centralwidget)
        self.label_Eye_of_Nature.setGeometry(QtCore.QRect(110, 257, 111, 21))
        font = QtGui.QFont()
        font.setFamily("Courier")
        font.setBold(True)
        font.setWeight(75)
        self.label_Eye_of_Nature.setFont(font)
        self.label_Eye_of_Nature.setObjectName("label_Eye_of_Nature")
        self.label_Violet_Gem = QtWidgets.QLabel(self.centralwidget)
        self.label_Violet_Gem.setGeometry(QtCore.QRect(110, 287, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Courier")
        font.setBold(True)
        font.setWeight(75)
        self.label_Violet_Gem.setFont(font)
        self.label_Violet_Gem.setObjectName("label_Violet_Gem")
        self.label_Frozen_Starlight = QtWidgets.QLabel(self.centralwidget)
        self.label_Frozen_Starlight.setGeometry(QtCore.QRect(110, 317, 141, 21))
        font = QtGui.QFont()
        font.setFamily("Courier")
        font.setBold(True)
        font.setWeight(75)
        self.label_Frozen_Starlight.setFont(font)
        self.label_Frozen_Starlight.setObjectName("label_Frozen_Starlight")
        self.label_Red_Sapphire = QtWidgets.QLabel(self.centralwidget)
        self.label_Red_Sapphire.setGeometry(QtCore.QRect(110, 347, 111, 21))
        font = QtGui.QFont()
        font.setFamily("Courier")
        font.setBold(True)
        font.setWeight(75)
        self.label_Red_Sapphire.setFont(font)
        self.label_Red_Sapphire.setObjectName("label_Red_Sapphire")
        self.label_Nature_Star = QtWidgets.QLabel(self.centralwidget)
        self.label_Nature_Star.setGeometry(QtCore.QRect(110, 377, 101, 16))
        font = QtGui.QFont()
        font.setFamily("Courier")
        font.setBold(True)
        font.setWeight(75)
        self.label_Nature_Star.setFont(font)
        self.label_Nature_Star.setObjectName("label_Nature_Star")
        self.label_Price = QtWidgets.QLabel(self.centralwidget)
        self.label_Price.setGeometry(QtCore.QRect(0, 20, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Courier")
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.label_Price.setFont(font)
        self.label_Price.setObjectName("label_Price")
        self.Button_Mistic_Violet_Ball = QtWidgets.QPushButton(self.centralwidget)
        self.Button_Mistic_Violet_Ball.setGeometry(QtCore.QRect(320, 39, 81, 31))
        self.Button_Mistic_Violet_Ball.setStyleSheet("background-color: rgb(255, 170, 255);")
        self.Button_Mistic_Violet_Ball.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("assets/Mistic_Violet_Ball_.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Button_Mistic_Violet_Ball.setIcon(icon)
        self.Button_Mistic_Violet_Ball.setIconSize(QtCore.QSize(100, 90))
        self.Button_Mistic_Violet_Ball.setFlat(False)
        self.Button_Mistic_Violet_Ball.setObjectName("Button_Mistic_Violet_Ball")
        self.Button_Mistic_Ball = QtWidgets.QPushButton(self.centralwidget)
        self.Button_Mistic_Ball.setGeometry(QtCore.QRect(320, 69, 81, 31))
        self.Button_Mistic_Ball.setStyleSheet("background-color: rgb(255, 170, 255);")
        self.Button_Mistic_Ball.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("assets/Mistic_Ball_.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Button_Mistic_Ball.setIcon(icon1)
        self.Button_Mistic_Ball.setIconSize(QtCore.QSize(100, 90))
        self.Button_Mistic_Ball.setObjectName("Button_Mistic_Ball")
        self.Button_Magic_Snowball = QtWidgets.QPushButton(self.centralwidget)
        self.Button_Magic_Snowball.setGeometry(QtCore.QRect(320, 130, 81, 31))
        self.Button_Magic_Snowball.setStyleSheet("background-color: rgb(255, 170, 255);")
        self.Button_Magic_Snowball.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("assets/Magic_Snowball.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Button_Magic_Snowball.setIcon(icon2)
        self.Button_Magic_Snowball.setIconSize(QtCore.QSize(100, 90))
        self.Button_Magic_Snowball.setObjectName("Button_Magic_Snowball")
        self.Button_Extra_Life = QtWidgets.QPushButton(self.centralwidget)
        self.Button_Extra_Life.setGeometry(QtCore.QRect(320, 99, 81, 31))
        self.Button_Extra_Life.setStyleSheet("background-color: rgb(255, 170, 255);")
        self.Button_Extra_Life.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("assets/extra_life1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Button_Extra_Life.setIcon(icon3)
        self.Button_Extra_Life.setIconSize(QtCore.QSize(100, 90))
        self.Button_Extra_Life.setObjectName("Button_Extra_Life")
        self.Button_Extra_Speed = QtWidgets.QPushButton(self.centralwidget)
        self.Button_Extra_Speed.setGeometry(QtCore.QRect(320, 160, 81, 31))
        self.Button_Extra_Speed.setStyleSheet("background-color: rgb(255, 170, 255);")
        self.Button_Extra_Speed.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("assets/extra_speed.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Button_Extra_Speed.setIcon(icon4)
        self.Button_Extra_Speed.setIconSize(QtCore.QSize(100, 90))
        self.Button_Extra_Speed.setObjectName("Button_Extra_Speed")
        self.Button_Falcon_Blue_Eye = QtWidgets.QPushButton(self.centralwidget)
        self.Button_Falcon_Blue_Eye.setGeometry(QtCore.QRect(320, 190, 81, 31))
        self.Button_Falcon_Blue_Eye.setStyleSheet("background-color: rgb(255, 170, 255);")
        self.Button_Falcon_Blue_Eye.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("assets/Falcon_Blue_Eye.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Button_Falcon_Blue_Eye.setIcon(icon5)
        self.Button_Falcon_Blue_Eye.setIconSize(QtCore.QSize(100, 90))
        self.Button_Falcon_Blue_Eye.setObjectName("Button_Falcon_Blue_Eye")
        self.Button_Elite_Sayian_Ball = QtWidgets.QPushButton(self.centralwidget)
        self.Button_Elite_Sayian_Ball.setGeometry(QtCore.QRect(320, 220, 81, 31))
        self.Button_Elite_Sayian_Ball.setStyleSheet("background-color: rgb(255, 170, 255);")
        self.Button_Elite_Sayian_Ball.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("assets/Elite_Saiyan_Ball.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Button_Elite_Sayian_Ball.setIcon(icon6)
        self.Button_Elite_Sayian_Ball.setIconSize(QtCore.QSize(100, 90))
        self.Button_Elite_Sayian_Ball.setObjectName("Button_Elite_Sayian_Ball")
        self.Button_Eye_of_Nature = QtWidgets.QPushButton(self.centralwidget)
        self.Button_Eye_of_Nature.setGeometry(QtCore.QRect(320, 250, 81, 31))
        self.Button_Eye_of_Nature.setStyleSheet("background-color: rgb(255, 170, 255);")
        self.Button_Eye_of_Nature.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("assets/Eye_of_Nature.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Button_Eye_of_Nature.setIcon(icon7)
        self.Button_Eye_of_Nature.setIconSize(QtCore.QSize(100, 90))
        self.Button_Eye_of_Nature.setObjectName("Button_Eye_of_Nature")
        self.Button_Violet_Gem = QtWidgets.QPushButton(self.centralwidget)
        self.Button_Violet_Gem.setGeometry(QtCore.QRect(320, 280, 81, 31))
        self.Button_Violet_Gem.setStyleSheet("background-color: rgb(255, 170, 255);")
        self.Button_Violet_Gem.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("assets/Violet_Gem.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Button_Violet_Gem.setIcon(icon8)
        self.Button_Violet_Gem.setIconSize(QtCore.QSize(100, 90))
        self.Button_Violet_Gem.setObjectName("Button_Violet_Gem")
        self.Button_Frozen_Starlight = QtWidgets.QPushButton(self.centralwidget)
        self.Button_Frozen_Starlight.setGeometry(QtCore.QRect(320, 310, 81, 31))
        self.Button_Frozen_Starlight.setStyleSheet("background-color: rgb(255, 170, 255);")
        self.Button_Frozen_Starlight.setText("")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("assets/Frozen_Starlight.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Button_Frozen_Starlight.setIcon(icon9)
        self.Button_Frozen_Starlight.setIconSize(QtCore.QSize(100, 90))
        self.Button_Frozen_Starlight.setObjectName("Button_Frozen_Starlight")
        self.Button_Red_Sapphire = QtWidgets.QPushButton(self.centralwidget)
        self.Button_Red_Sapphire.setGeometry(QtCore.QRect(320, 340, 81, 31))
        self.Button_Red_Sapphire.setStyleSheet("background-color: rgb(255, 170, 255);")
        self.Button_Red_Sapphire.setText("")
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap("assets/Red_Sapphire.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Button_Red_Sapphire.setIcon(icon10)
        self.Button_Red_Sapphire.setIconSize(QtCore.QSize(100, 90))
        self.Button_Red_Sapphire.setObjectName("Button_Red_Sapphire")
        self.Button_Nature_Star = QtWidgets.QPushButton(self.centralwidget)
        self.Button_Nature_Star.setGeometry(QtCore.QRect(320, 370, 81, 31))
        self.Button_Nature_Star.setStyleSheet("background-color: rgb(255, 170, 255);")
        self.Button_Nature_Star.setText("")
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap("assets/Nature_Star.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Button_Nature_Star.setIcon(icon11)
        self.Button_Nature_Star.setIconSize(QtCore.QSize(100, 90))
        self.Button_Nature_Star.setObjectName("Button_Nature_Star")
        self.label_selection = QtWidgets.QLabel(self.centralwidget)
        self.label_selection.setGeometry(QtCore.QRect(250, 10, 201, 20))
        font = QtGui.QFont()
        font.setFamily("Courier")
        font.setBold(True)
        font.setWeight(75)
        self.label_selection.setFont(font)
        self.label_selection.setObjectName("label_selection")
        self.label_your_gold = QtWidgets.QLabel(self.centralwidget)
        self.label_your_gold.setGeometry(QtCore.QRect(0, 0, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Courier")
        self.label_your_gold.setFont(font)
        self.label_your_gold.setObjectName("label_your_gold")
        self.label_gold = QtWidgets.QLabel(self.centralwidget)
        self.label_gold.setGeometry(QtCore.QRect(90, 5, 81, 16))
        font = QtGui.QFont()
        font.setFamily("Courier")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_gold.setFont(font)
        self.label_gold.setStyleSheet("border-color: rgb(0, 0, 0);")
        self.label_gold.setText("")
        self.label_gold.setObjectName("label_gold")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 450, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.Button_Mistic_Violet_Ball.clicked.connect(self.MisticVioletBall)
        self.Button_Mistic_Ball.clicked.connect(self.MisticBall)
        self.Button_Extra_Life.clicked.connect(self.ExtraLife)
        self.Button_Magic_Snowball.clicked.connect(self.MagicSnowball)
        self.Button_Extra_Speed.clicked.connect(self.ExtraSpeed)
        self.Button_Falcon_Blue_Eye.clicked.connect(self.FalconBlueEye)
        self.Button_Elite_Sayian_Ball.clicked.connect(self.EliteSayianBall)
        self.Button_Eye_of_Nature.clicked.connect(self.EyeofNature)
        self.Button_Violet_Gem.clicked.connect(self.VioletGem)
        self.Button_Frozen_Starlight.clicked.connect(self.FrozenStarlight)
        self.Button_Red_Sapphire.clicked.connect(self.RedSapphire)
        self.Button_Nature_Star.clicked.connect(self.NatureStar)


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_11000.setText(_translate("MainWindow", "11000"))
        self.label_10000.setText(_translate("MainWindow", "10000"))
        self.label_9000.setText(_translate("MainWindow", "9000"))
        self.label_8000.setText(_translate("MainWindow", "8000"))
        self.label_7000.setText(_translate("MainWindow", "7000"))
        self.label_6000.setText(_translate("MainWindow", "6000"))
        self.label_5000.setText(_translate("MainWindow", "5000"))
        self.label_4000.setText(_translate("MainWindow", "4000"))
        self.label_3000.setText(_translate("MainWindow", "3000"))
        self.label_2000.setText(_translate("MainWindow", "2000"))
        self.label_1000.setText(_translate("MainWindow", "1000"))
        self.label_12000.setText(_translate("MainWindow", "12000"))
        self.label_Mistic_Violet_Ball.setText(_translate("MainWindow", "Mistic Violet Ball"))
        self.label_Mistic_Ball.setText(_translate("MainWindow", "Mistic Ball"))
        self.label_Extra_Life.setText(_translate("MainWindow", "Extra Life"))
        self.label_Magic_Snowball.setText(_translate("MainWindow", "Magic Snowball"))
        self.label_Extra_Speed.setText(_translate("MainWindow", "Extra Speed"))
        self.label_Falcon_Blue_Eye.setText(_translate("MainWindow", "Falcon Blue Eye"))
        self.label_Elite_Sayian_Ball.setText(_translate("MainWindow", "Elite Sayian Ball"))
        self.label_Eye_of_Nature.setText(_translate("MainWindow", "Eye of Nature"))
        self.label_Violet_Gem.setText(_translate("MainWindow", "Violet Gem"))
        self.label_Frozen_Starlight.setText(_translate("MainWindow", "Frozen Starlight"))
        self.label_Red_Sapphire.setText(_translate("MainWindow", "Red Sapphire"))
        self.label_Nature_Star.setText(_translate("MainWindow", "Nature Star"))
        self.label_Price.setText(_translate("MainWindow", "Price:"))
        self.label_selection.setText(_translate("MainWindow", "Select to buy:"))
        self.label_your_gold.setText(_translate("MainWindow", "Your gold:"))

    def MisticVioletBall(self):
        """
        Funkcja odpowiedzialna za sprzedaż konkretnej broni oraz przestawienie atrybutów gracza
        """
        if player_gui.gold >= 12000:
            player_gui.laser_img = pygame.image.load(os.path.join("assets", "Mistic_Violet_Ball_.png"))
            player_gui.attack = 110
            player_gui.COOLDOWN = 10
            player_gui.laser_velocity = 15
            player_gui.gold -= 12000
            self.label_gold.setText(str(player_gui.gold))
            self.label_selection.setText("Bought Mistic Violet Ball")
        else:
            self.label_selection.setText("You are out of money")

    def MisticBall(self):
        """
        Funkcja odpowiedzialna za sprzedaż konkretnej broni oraz przestawienie atrybutów gracza
        """
        if player_gui.gold >= 11000:
            player_gui.laser_img = pygame.image.load(os.path.join("assets", "Mistic_Ball_.png"))
            player_gui.attack = 100
            player_gui.COOLDOWN = 12
            player_gui.laser_velocity = 14
            player_gui.gold -= 11000
            self.label_gold.setText(str(player_gui.gold))
            self.label_selection.setText("Bought Mistic Ball")
        else:
            self.label_selection.setText("You are out of money")

    def ExtraLife(self):
        """
        Funkcja odpowiedzialna za sprzedaż usługi oraz przestawienie atrybutów gracza
        """
        if player_gui.gold >= 10000:
            player_gui.lives += 1
            player_gui.gold -= 10000
            self.label_gold.setText(str(player_gui.gold))
            self.label_selection.setText("Bought Extra Life")
        else:
            self.label_selection.setText("You are out of money")

    def MagicSnowball(self):
        """
        Funkcja odpowiedzialna za sprzedaż konkretnej broni oraz przestawienie atrybutów gracza
        """
        if player_gui.gold >= 9000:
         player_gui.laser_img = pygame.image.load(os.path.join("assets", "Magic_Snowball.png"))
         player_gui.attack = 90
         player_gui.COOLDOWN = 14
         player_gui.laser_velocity = 13
         player_gui.gold -= 9000
         self.label_gold.setText(str(player_gui.gold))
         self.label_selection.setText("Bought Magic Snowball")
        else:
            self.label_selection.setText("You are out of money")

    def ExtraSpeed(self):
        """
        Funkcja odpowiedzialna za sprzedaż usługi oraz przestawienie atrybutów gracza
        """
        if player_gui.gold >= 8000:
             player_gui.velocity += 5
             player_gui.gold -= 8000
             self.label_gold.setText(str(player_gui.gold))
             self.label_selection.setText("Bought Extra Speed")
        else:
             self.label_selection.setText("You are out of money")

    def FalconBlueEye(self):
        """
        Funkcja odpowiedzialna za sprzedaż konkretnej broni oraz przestawienie atrybutów gracza
        """
        if player_gui.gold >= 7000:
         player_gui.laser_img = pygame.image.load(os.path.join("assets", "Falcon_Blue_Eye.png"))
         player_gui.attack = 80
         player_gui.COOLDOWN = 16
         player_gui.laser_velocity = 12
         player_gui.gold -= 7000
         self.label_gold.setText(str(player_gui.gold))
         self.label_selection.setText("Bought Falcon Blue Eye")
        else:
            self.label_selection.setText("You are out of money")

    def EliteSayianBall(self):
        """
        Funkcja odpowiedzialna za sprzedaż konkretnej broni oraz przestawienie atrybutów gracza
        """
        if player_gui.gold >= 6000:
         player_gui.laser_img = pygame.image.load(os.path.join("assets", "Elite_Saiyan_Ball.png"))
         player_gui.attack = 70
         player_gui.COOLDOWN = 18
         player_gui.laser_velocity = 11
         player_gui.gold -= 6000
         self.label_gold.setText(str(player_gui.gold))
         self.label_selection.setText("Bought Elite Sayian Ball")
        else:
            self.label_selection.setText("You are out of money")

    def EyeofNature(self):
        """
        Funkcja odpowiedzialna za sprzedaż konkretnej broni oraz przestawienie atrybutów gracza
        """
        if player_gui.gold >= 5000:
         player_gui.laser_img = pygame.image.load(os.path.join("assets", "Eye_of_Nature.png"))
         player_gui.attack = 60
         player_gui.COOLDOWN = 20
         player_gui.laser_velocity = 10
         player_gui.gold -= 5000
         self.label_gold.setText(str(player_gui.gold))
         self.label_selection.setText("Bought Eye of Nature")
        else:
            self.label_selection.setText("You are out of money")

    def VioletGem(self):
        """
        Funkcja odpowiedzialna za sprzedaż konkretnej broni oraz przestawienie atrybutów gracza
        """
        if player_gui.gold >= 4000:
         player_gui.laser_img = pygame.image.load(os.path.join("assets", "Violet_Gem.png"))
         player_gui.attack = 50
         player_gui.COOLDOWN = 22
         player_gui.laser_velocity = 9
         player_gui.gold -= 4000
         self.label_gold.setText(str(player_gui.gold))
         self.label_selection.setText("Bought Violet Gem")
        else:
            self.label_selection.setText("You are out of money")

    def FrozenStarlight(self):
        """
        Funkcja odpowiedzialna za sprzedaż konkretnej broni oraz przestawienie atrybutów gracza
        """
        if player_gui.gold >= 3000:
         player_gui.laser_img = pygame.image.load(os.path.join("assets", "Frozen_Starlight.png"))
         player_gui.attack = 40
         player_gui.COOLDOWN = 24
         player_gui.laser_velocity = 8
         player_gui.gold -= 3000
         self.label_gold.setText(str(player_gui.gold))
         self.label_selection.setText("Bought Frozen Starlight")
        else:
            self.label_selection.setText("You are out of money")

    def RedSapphire(self):
        """
        Funkcja odpowiedzialna za sprzedaż konkretnej broni oraz przestawienie atrybutów gracza
        """
        if player_gui.gold >= 2000:
         player_gui.laser_img = pygame.image.load(os.path.join("assets", "Red_Sapphire.png"))
         player_gui.attack = 30
         player_gui.COOLDOWN = 26
         player_gui.laser_velocity = 7
         player_gui.gold -= 2000
         self.label_gold.setText(str(player_gui.gold))
         self.label_selection.setText("Bought Red Sapphire")
        else:
            self.label_selection.setText("You are out of money")

    def NatureStar(self):
        """
        Funkcja odpowiedzialna za sprzedaż konkretnej broni oraz przestawienie atrybutów gracza
        """
        if player_gui.gold >= 1000:
         player_gui.laser_img = pygame.image.load(os.path.join("assets", "Nature_Star.png"))
         player_gui.attack = 20
         player_gui.COOLDOWN = 28
         player_gui.laser_velocity = 6
         player_gui.gold -= 1000
         self.label_gold.setText(str(player_gui.gold))
         self.label_selection.setText("Bought Nature Star")
        else:
            self.label_selection.setText("You are out of money")

app = QtWidgets.QApplication(sys.argv)

def store_4(player):
    """
    Funkcja odpowiedzialna za otworzenie gui
    """
    global MainWindow
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    global player_gui
    player_gui = player
    ui.label_gold.setText(str(player_gui.gold))
    MainWindow.show()
    app.exec_()
