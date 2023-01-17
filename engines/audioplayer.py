from playsound import playsound
import os

def Play(directory, block):
    audio = os.getcwd() + directory
    playsound(audio, block)