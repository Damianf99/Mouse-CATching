from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        """
        Główna klasa gui od zapisu do pliku
        """
        MainWindow.setObjectName("Mouse CATching")
        MainWindow.resize(450, 450)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 450, 450))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("assets/tlo.png"))
        self.label.setObjectName("label")
        self.EnterNameBar = QtWidgets.QLineEdit(self.centralwidget)
        self.EnterNameBar.setGeometry(QtCore.QRect(110, 120, 221, 21))
        self.EnterNameBar.setClearButtonEnabled(False)
        self.EnterNameBar.setObjectName("EnterNameBar")
        self.SaveButton = QtWidgets.QPushButton(self.centralwidget)
        self.SaveButton.setGeometry(QtCore.QRect(350, 118, 75, 23))
        self.SaveButton.setObjectName("SaveButton")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 80, 211, 31))
        font = QtGui.QFont()
        font.setFamily("Courier")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.second_name_label = QtWidgets.QLabel(self.centralwidget)
        self.second_name_label.setGeometry(QtCore.QRect(150, 200, 101, 20))
        font = QtGui.QFont()
        font.setFamily("Courier")
        self.second_name_label.setFont(font)
        self.second_name_label.setText("")
        self.second_name_label.setObjectName("second_name_label")
        self.third_name_label = QtWidgets.QLabel(self.centralwidget)
        self.third_name_label.setGeometry(QtCore.QRect(150, 220, 101, 20))
        font = QtGui.QFont()
        font.setFamily("Courier")
        self.third_name_label.setFont(font)
        self.third_name_label.setText("")
        self.third_name_label.setObjectName("third_name_label")
        self.first_name_label = QtWidgets.QLabel(self.centralwidget)
        self.first_name_label.setGeometry(QtCore.QRect(150, 180, 101, 20))
        font = QtGui.QFont()
        font.setFamily("Courier")
        self.first_name_label.setFont(font)
        self.first_name_label.setText("")
        self.first_name_label.setObjectName("first_name_label")
        self.fourth_name_label = QtWidgets.QLabel(self.centralwidget)
        self.fourth_name_label.setGeometry(QtCore.QRect(150, 240, 101, 20))
        font = QtGui.QFont()
        font.setFamily("Courier")
        self.fourth_name_label.setFont(font)
        self.fourth_name_label.setText("")
        self.fourth_name_label.setObjectName("fourth_name_label")
        self.fifth_name_label = QtWidgets.QLabel(self.centralwidget)
        self.fifth_name_label.setGeometry(QtCore.QRect(150, 260, 101, 20))
        font = QtGui.QFont()
        font.setFamily("Courier")
        self.fifth_name_label.setFont(font)
        self.fifth_name_label.setText("")
        self.fifth_name_label.setObjectName("fifth_name_label")
        self.sixth_name_label = QtWidgets.QLabel(self.centralwidget)
        self.sixth_name_label.setGeometry(QtCore.QRect(150, 280, 101, 20))
        font = QtGui.QFont()
        font.setFamily("Courier")
        self.sixth_name_label.setFont(font)
        self.sixth_name_label.setText("")
        self.sixth_name_label.setObjectName("sixth_name_label")
        self.seventh_name_label = QtWidgets.QLabel(self.centralwidget)
        self.seventh_name_label.setGeometry(QtCore.QRect(150, 300, 101, 20))
        font = QtGui.QFont()
        font.setFamily("Courier")
        self.seventh_name_label.setFont(font)
        self.seventh_name_label.setText("")
        self.seventh_name_label.setObjectName("seventh_name_label")
        self.eighth_name_label = QtWidgets.QLabel(self.centralwidget)
        self.eighth_name_label.setGeometry(QtCore.QRect(150, 320, 101, 20))
        font = QtGui.QFont()
        font.setFamily("Courier")
        self.eighth_name_label.setFont(font)
        self.eighth_name_label.setText("")
        self.eighth_name_label.setObjectName("eighth_name_label")
        self.nineth_name_label = QtWidgets.QLabel(self.centralwidget)
        self.nineth_name_label.setGeometry(QtCore.QRect(150, 340, 101, 20))
        font = QtGui.QFont()
        font.setFamily("Courier")
        self.nineth_name_label.setFont(font)
        self.nineth_name_label.setText("")
        self.nineth_name_label.setObjectName("nineth_name_label")
        self.tenth_name_label = QtWidgets.QLabel(self.centralwidget)
        self.tenth_name_label.setGeometry(QtCore.QRect(150, 360, 101, 20))
        font = QtGui.QFont()
        font.setFamily("Courier")
        self.tenth_name_label.setFont(font)
        self.tenth_name_label.setText("")
        self.tenth_name_label.setObjectName("tenth_name_label")
        self.HighscoreButton = QtWidgets.QPushButton(self.centralwidget)
        self.HighscoreButton.setGeometry(QtCore.QRect(190, 150, 101, 23))
        self.HighscoreButton.setObjectName("HighscoreButton")
        self.first_score_label = QtWidgets.QLabel(self.centralwidget)
        self.first_score_label.setGeometry(QtCore.QRect(260, 180, 101, 20))
        font = QtGui.QFont()
        font.setFamily("Courier")
        self.first_score_label.setFont(font)
        self.first_score_label.setText("")
        self.first_score_label.setObjectName("first_score_label")
        self.second_score_label = QtWidgets.QLabel(self.centralwidget)
        self.second_score_label.setGeometry(QtCore.QRect(260, 200, 101, 20))
        font = QtGui.QFont()
        font.setFamily("Courier")
        self.second_score_label.setFont(font)
        self.second_score_label.setText("")
        self.second_score_label.setObjectName("second_score_label")
        self.third_score_label = QtWidgets.QLabel(self.centralwidget)
        self.third_score_label.setGeometry(QtCore.QRect(260, 220, 101, 20))
        font = QtGui.QFont()
        font.setFamily("Courier")
        self.third_score_label.setFont(font)
        self.third_score_label.setText("")
        self.third_score_label.setObjectName("third_score_label")
        self.fourth_score_label = QtWidgets.QLabel(self.centralwidget)
        self.fourth_score_label.setGeometry(QtCore.QRect(260, 240, 101, 20))
        font = QtGui.QFont()
        font.setFamily("Courier")
        self.fourth_score_label.setFont(font)
        self.fourth_score_label.setText("")
        self.fourth_score_label.setObjectName("fourth_score_label")
        self.fifth_score_label = QtWidgets.QLabel(self.centralwidget)
        self.fifth_score_label.setGeometry(QtCore.QRect(260, 260, 101, 20))
        font = QtGui.QFont()
        font.setFamily("Courier")
        self.fifth_score_label.setFont(font)
        self.fifth_score_label.setText("")
        self.fifth_score_label.setObjectName("fifth_score_label")
        self.sixth_score_label = QtWidgets.QLabel(self.centralwidget)
        self.sixth_score_label.setGeometry(QtCore.QRect(260, 280, 101, 20))
        font = QtGui.QFont()
        font.setFamily("Courier")
        self.sixth_score_label.setFont(font)
        self.sixth_score_label.setText("")
        self.sixth_score_label.setObjectName("sixth_score_label")
        self.seventh_score_label = QtWidgets.QLabel(self.centralwidget)
        self.seventh_score_label.setGeometry(QtCore.QRect(260, 300, 101, 20))
        font = QtGui.QFont()
        font.setFamily("Courier")
        self.seventh_score_label.setFont(font)
        self.seventh_score_label.setText("")
        self.seventh_score_label.setObjectName("seventh_score_label")
        self.eighth_score_label = QtWidgets.QLabel(self.centralwidget)
        self.eighth_score_label.setGeometry(QtCore.QRect(260, 320, 101, 20))
        font = QtGui.QFont()
        font.setFamily("Courier")
        self.eighth_score_label.setFont(font)
        self.eighth_score_label.setText("")
        self.eighth_score_label.setObjectName("eighth_score_label")
        self.nineth_score_label = QtWidgets.QLabel(self.centralwidget)
        self.nineth_score_label.setGeometry(QtCore.QRect(260, 340, 101, 20))
        font = QtGui.QFont()
        font.setFamily("Courier")
        self.nineth_score_label.setFont(font)
        self.nineth_score_label.setText("")
        self.nineth_score_label.setObjectName("nineth_score_label")
        self.tenth_score_label = QtWidgets.QLabel(self.centralwidget)
        self.tenth_score_label.setGeometry(QtCore.QRect(260, 360, 101, 20))
        font = QtGui.QFont()
        font.setFamily("Courier")
        self.tenth_score_label.setFont(font)
        self.tenth_score_label.setText("")
        self.tenth_score_label.setObjectName("tenth_score_label")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 10, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Courier")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.Score_label = QtWidgets.QLabel(self.centralwidget)
        self.Score_label.setGeometry(QtCore.QRect(150, 10, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Courier")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.Score_label.setFont(font)
        self.Score_label.setText("")
        self.Score_label.setObjectName("Score_label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 450, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.HighscoreButton.clicked.connect(self.highscore_button)
        self.SaveButton.clicked.connect(self.save_button)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.SaveButton.setText(_translate("MainWindow", "Save"))
        self.label_2.setText(_translate("MainWindow", "Enter your name:"))
        self.HighscoreButton.setText(_translate("MainWindow", "Show Highscores"))
        self.label_3.setText(_translate("MainWindow", "Your Score:"))
    
    def save_button(self):
        """
        Przycisk odpowiedzialny za zapis do pliku
        """
        global saved
        if saved == False:
            player_gui.name = self.EnterNameBar.text()
            f = open('gui_gra/Score.txt', 'a')
            f.write(str(player_gui.score))
            f.write("\n")
            f.write(player_gui.name)
            f.write("\n")
            f.close()
            extract_data()
            saved = True
        else:
            return

    def highscore_button(self):
        """
        Funkcja odpowiedzialna za odczyt z pliku
        """
        SortedList = extract_data()
        LabelList = [[self.first_name_label, self.first_score_label],
                 [self.second_name_label, self.second_score_label],
                 [self.third_name_label, self.third_score_label],
                 [self.fourth_name_label, self.fourth_score_label],
                 [self.fifth_name_label, self.fifth_score_label],
                 [self.sixth_name_label, self.sixth_score_label],
                 [self.seventh_name_label, self.seventh_score_label],
                 [self.eighth_name_label, self.eighth_score_label],
                 [self.nineth_name_label, self.nineth_score_label],
                 [self.tenth_name_label, self.tenth_score_label]]
        for i in range(0,len(SortedList)):
            LabelList[i][0].setText(SortedList[i][0])
            LabelList[i][1].setText(str(SortedList[i][1]))

def extract_data():
    """
    Funkcja odpowiedzialna za przetwarzanie danych z pliku
    """
    f = open('gui_gra/Score.txt','r')
    line = f.readline()
    lista = []
    while line != '':
        lista.append(line.replace('\n', ''))
        line = f.readline()

    f.close()

    for i in range(0,len(lista),2):
        lista[i] = int(lista[i])

    NewList = []
    for i in range(0,len(lista),2):
        NewList.append([lista[i], lista[i+1]])

    NewList.sort()
    SortedList = []
    for i in range(len(NewList)-1,-1,-1):
        SortedList.append([NewList[i][1], NewList[i][0]])

    if len(SortedList) < 10:
        size = len(SortedList)
    else:
        size = 10

    f = open('gui_gra/Score.txt', 'w')
    for i in range(size):
        f.write(str(SortedList[i][1]))
        f.write("\n")
        f.write(SortedList[i][0])
        f.write("\n")
    f.close()
    return SortedList

saved = False

def save_name(player):
    """
    Funkcja odpowiedzialna za otworzenie gui
    """
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    global player_gui
    player_gui = player
    ui.Score_label.setText(str(player_gui.score))
    MainWindow.show()
    app.exec_()