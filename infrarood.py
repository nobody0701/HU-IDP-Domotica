import RPi.GPIO as GPIO
from time import sleep

def Infrarood(stat):
    if stat == False:
        return False
    else:
        GPIO.setmode(GPIO.BCM)     # gebruik nummering achter GPIO op afbeelding
        GPIO.setup(26, GPIO.IN)

        lazer = GPIO.input(26)
        if lazer == 0:  #iets gedetecteerd
            infrood = True
            print("opstakel gedetecteerd")
        elif lazer == 1: #niks gedetecteerd
            print("niks gedetecteerd")
            infrood = False
        return infrood
