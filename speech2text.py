import speech_recognition as sr


def Start():
    # get audio from the microphone
    r = sr.Recognizer()
    with sr.Microphone() as source:
        #print("Speak:")
        audio = r.listen(source)

    try:
        text2return = r.recognize_google(audio)+ " "
        return text2return
    except sr.UnknownValueError:
        #print("Could not understand audio")
        return "Could not understand audio"
    except sr.RequestError as e:
        #print("Could not request results; {0}".format(e))
        return "Could not request results; {0}".format(e)
