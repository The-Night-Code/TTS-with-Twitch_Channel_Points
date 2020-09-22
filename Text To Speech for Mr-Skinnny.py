from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
import pyttsx3

try:
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    url = "https://www.twitch.tv/popout/skinnny/chat?popout="
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get(url)

    while True:
        try:
            Texts = driver.find_elements_by_class_name('chat-line__message-body--highlighted')
            #Texts = driver.find_elements_by_class_name("chat-line__message")
            for x in range(0, len(Texts)):
                text = Texts[x].text
                driver.refresh()
                
                engine.setProperty('voice', voices[0].id) # " voices[0] " for male voice / " voices[1] " for female voice
                
                engine.setProperty('volume', 5) # volume from 0 to 10
                
                engine.setProperty('rate', 100) # rate from 0 to 200
                engine.say(text)
                engine.runAndWait()

        except:
            pass

except:
    pass
