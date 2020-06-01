from PyQt5.QtWidgets import QMainWindow,QApplication
from PyQt5.QtGui import QIcon
from PySide2.QtTextToSpeech import QTextToSpeech
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from main_window_UI_1 import Ui_MainWindow
#from PyQt5 import QtCore, QtWidgets
#from os import path
#from PyQt5.uic import loadUiType
#import sys


#FROM_CLASS, _ = loadUiType(path.join(path.dirname(__file__), "main_window_UI_1.ui"))

FROM_CLASS = Ui_MainWindow
class MainApp(QMainWindow, FROM_CLASS):
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
            self.setWindowTitle('TTS for High-light Message in Twitch')
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
        self.setFixedSize(643, 400)

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
            try:
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

            except:
                pass

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
