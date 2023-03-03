from gtts import gTTS
import tkinter as tk
from tempfile import TemporaryFile
from time import sleep
import os
import pyglet


def playAudio(text1):

    #from gtts import gTTS

    text2speech1 = gTTS(text1, lang='en')
    filename = "temp.wav"
    text2speech1.save(filename)
    #music = pyglet.media.load(filename, streaming=False)
    music = pyglet.resource.media(filename)
    music.play()
    sleep(music.duration) #prevent from killing
    os.remove(filename) #remove temperory file


playAudio("They flesh consumed")