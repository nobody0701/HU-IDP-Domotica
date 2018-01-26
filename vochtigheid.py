import RPi.GPIO as GPIO
from time import sleep

def Vochtigheid():
    GPIO.setmode(GPIO.BCM)     # gebruik nummering achter GPIO op afbeelding
    GPIO.setup(25, GPIO.IN)    # nummer 25 als input, vocht = LOW
    #GPIO.setup(14, GPIO.IN)
    #GPIO.setup(15, GPIO.IN)

    try:
        if GPIO.input(25): # if port 25 == 1 #vochtsensor
            vocht = False
            print("1/GPIO.HIGH/True") #high is droog

        else:
            vocht = True
            print("0/GPIO.LOW/False")
        return vocht

    except KeyboardInterrupt:
        GPIO.cleanup()
