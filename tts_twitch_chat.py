from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pyttsx3
import pyttsx3.drivers.sapi5
from tkinter import *


win= Tk()
win.title("TTS")
win.resizable(0,0)


#get the name of the twitch channel
Label(win, text="Just enter the twitch channel name").pack()
entree = Entry(win, width=30)
entree.pack()


def tts_twitch_start():
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice',voices[0].id)
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get("https://www.twitch.tv/" + str(entree.get()))


    #Texts = driver.find_elements_by_xpath('//*[@id="93ef4f4941fdb3dd4d649d57848696d2"]/div/div[1]/div/div/section/div/div[3]/div[2]/div[3]/div/div/div[16]/div/div[2]/div')
    while True:
        Texts = driver.find_elements_by_class_name('chat-line__message-body--highlighted')

        def speak(text):
            engine.say(text)
            engine.runAndWait()

        for x in range (0, len(Texts)):
            print(Texts[x].text)
            text = Texts[x].text
            speak(text)
            driver.refresh()

Button(win, text= "START",command=tts_twitch_start ).pack()


win.mainloop()