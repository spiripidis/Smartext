import pyttsx3
#import pyttsx3.drivers.sapi5
#pyttsx needs to be ==2.71


def text2speech(somestring):

    engine = pyttsx3.init()
    engine.setProperty('rate', 60)
    engine.setProperty('volume', 0.9)
    engine.say(somestring)
    engine.runAndWait()


