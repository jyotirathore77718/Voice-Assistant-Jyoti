import  os
import pyttsx3
engine = pyttsx3.init()
def Speak(T):
    engine.say(T)
    engine.runAndWait()