from PyQt5.QtWidgets import QMainWindow,QApplication
from PyQt5.QtGui import QIcon
from PySide2.QtTextToSpeech import QTextToSpeech
from PyQt5 import QtCore, QtWidgets
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(530, 563)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(410, 60, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(70, 60, 211, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(60, 10, 231, 61))
        self.label.setObjectName("label")
        self.volumeSlider = QtWidgets.QSlider(self.centralwidget)
        self.volumeSlider.setGeometry(QtCore.QRect(120, 110, 101, 22))
        self.volumeSlider.setMaximum(100)
        self.volumeSlider.setProperty("value", 50)
        self.volumeSlider.setOrientation(QtCore.Qt.Horizontal)
        self.volumeSlider.setObjectName("volumeSlider")
        self.rateSlider = QtWidgets.QSlider(self.centralwidget)
        self.rateSlider.setGeometry(QtCore.QRect(120, 140, 101, 22))
        self.rateSlider.setMaximum(100)
        self.rateSlider.setProperty("value", 25)
        self.rateSlider.setOrientation(QtCore.Qt.Horizontal)
        self.rateSlider.setObjectName("rateSlider")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(50, 140, 47, 13))
        self.label_2.setObjectName("label_2")
        self.voiceCombo = QtWidgets.QComboBox(self.centralwidget)
        self.voiceCombo.setGeometry(QtCore.QRect(120, 180, 181, 22))
        self.voiceCombo.setObjectName("voiceCombo")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(50, 110, 47, 13))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(50, 180, 47, 13))
        self.label_4.setObjectName("label_4")
        self.checkBox_username = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_username.setGeometry(QtCore.QRect(70, 220, 191, 17))
        self.checkBox_username.setObjectName("checkBox_username")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(10, 280, 341, 41))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(10, 320, 521, 16))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(10, 350, 391, 21))
        self.label_7.setObjectName("label_7")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 530, 21))
        self.menubar.setObjectName("menubar")
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionHelp = QtWidgets.QAction(MainWindow)
        self.actionHelp.setObjectName("actionHelp")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.menuAbout.addAction(self.actionHelp)
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "START"))
        self.label.setWhatsThis(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt; font-weight:600;\">Just enter the twitch channel name:</span></p></body></html>"))
        self.label.setText(_translate("MainWindow", "Just enter the twitch channel name:"))
        self.label_2.setText(_translate("MainWindow", "Speed"))
        self.label_3.setText(_translate("MainWindow", "Volume"))
        self.label_4.setText(_translate("MainWindow", "Voice"))
        self.checkBox_username.setText(_translate("MainWindow", "You will not pronounce the n-word"))
        self.label_5.setText(_translate("MainWindow", "The program need Google Chrome to run, so please don\'t close is."))
        self.label_6.setText(_translate("MainWindow", "Make sure that GOOGLE CHROME is closed if you wanna change the volume of the sound or voice speed."))
        self.label_7.setText(_translate("MainWindow", "If Google Chrome is open, please don\'t touch the app, due to a coding problem."))
        self.menuAbout.setTitle(_translate("MainWindow", "Help"))
        self.actionHelp.setText(_translate("MainWindow", "Help"))
        self.actionAbout.setText(_translate("MainWindow", "About"))




class MainApp(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainApp, self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.Handel_UI()
        self.Handel_Buttons()

        self.engine = None
        engineNames = QTextToSpeech.availableEngines()
        if len(engineNames) > 0:
            engineName = engineNames[0]
            self.engine = QTextToSpeech(engineName)
            self.engine.stateChanged.connect(self.stateChanged)
            self.setWindowTitle('TTS for Highlight Message in Twitch')
            self.setWindowIcon(QIcon('tts icon 2.png'))
            self.voices = []
            for voice in self.engine.availableVoices():
                self.voices.append(voice)
                self.voiceCombo.addItem(voice.name())
        else:
            self.setWindowTitle('TTS for Highlight Message in Twitch (no engines available)')
            self.sayButton.setEnabled(False)



    def Handel_UI(self):
        self.setWindowTitle("TTS for Highlight Message in Twitch asdfg")
        self.setFixedSize(530, 420)

    def Handel_Buttons(self):
        self.pushButton.clicked.connect(self.say)
        self.actionHelp.triggered.connect(self.help_window)


    # place where i write my code
    # def
    def say(self):
        url = self.lineEdit.text()

        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get("https://www.twitch.tv/" + url)

        while True:
            Texts = driver.find_elements_by_class_name('chat-line__message-body--highlighted')
            for x in range(0, len(Texts)):
                text = Texts[x].text
                self.engine.setVoice(self.voices[self.voiceCombo.currentIndex()])
                self.engine.setVolume(float(self.volumeSlider.value()) / 100)
                self.engine.setRate(int(self.rateSlider.value()) / 100)

                if self.checkBox_username.isChecked():
                    texttest = ["nigger", "zin g", "niger", "niggest", "nibber", "niber", "n.i.g.g.e.r", "n.i.g.e.r"]
                    if any(word in text.lower() for word in texttest):
                        driver.refresh()
                    else:
                        self.engine.say(text)
                        driver.refresh()
                else:
                    self.engine.say(text)
                    driver.refresh()

    def stateChanged(self, state):
        if (state == QTextToSpeech.State.Ready):
            self.sayButton.setEnabled(True)

    def help_window(self):
        pass

def main():
    app = QApplication([])
    MainApplication = MainApp()
    MainApplication.show()
    app.exec()


if __name__ == '__main__':
    main()