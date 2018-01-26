import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)     # gebruik nummering achter GPIO op afbeelding
GPIO.setup(26, GPIO.IN)

while True:
    lazer = GPIO.input(26)

    if lazer==0:  #iets gedetecteerd
        print("opstakel gedetecteerd")
        sleep(1.0)
    elif lazer==1: #niks gedetecteerd
        print("niks gedetecteerd")
        sleep(1.0)

