from selenium import webdriver
import pyttsx3
from tkinter import *

win = Tk()
win.title("TTS")
win.resizable(0,0)

img = PhotoImage(file='tts icon.ico')
win.tk.call('wm', 'iconphoto', win._w, img)

#get the name of the twitch channel
Label(win, text="Just enter the twitch channel name").grid()
entree = Entry(win, width=30)
entree.grid()


def tts_twitch_start():
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice',voices[0].id)
    driver = webdriver.Chrome('D:\Project\Project\Rebot Router\chromedriver11.exe')
    driver.get("https://www.twitch.tv/" + str(entree.get()))

    #Texts = driver.find_elements_by_xpath('//*[@id="93ef4f4941fdb3dd4d649d57848696d2"]/div/div[1]/div/div/section/div/div[3]/div[2]/div[3]/div/div/div[16]/div/div[2]/div')
    while True:
        Texts = driver.find_elements_by_class_name('chat-line__message-body--highlighted')

        def speak(text):
            engine.say(text)
            engine.runAndWait()

        for x in range (0, len(Texts)):
            text1 = Texts[x].text
            # if ther is n-word in the text1 the program will be restart
            # the browser will be refresh 
            # and if ther is no n-word the programm will be complet working
            texttest = ["nigger", "zin g", "niger","niggest","nibber","niber","n.i.g.g.e.r","n.i.g.e.r"]
            if any(word in text1.lower() for word in texttest):
                driver.refresh()
            else:
                speak(text1)
                driver.refresh()


Button(win, text= "START",command=tts_twitch_start ).grid()

s = Scale(win, from_ = 0, to=100, orient=HORIZONTAL, length=200, width=10, sliderlength=50)
s.set(50)
s.grid()

win.mainloop()
