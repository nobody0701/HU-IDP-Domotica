import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)     # gebruik nummering achter GPIO op afbeelding
GPIO.setup(25, GPIO.IN)    # nummer 25 als input, vocht = LOW
#GPIO.setup(14, GPIO.IN)
#GPIO.setup(15, GPIO.IN)

try:
    while True:
        if GPIO.input(25): # if port 25 == 1 #vochtsensor
            print("1/GPIO.HIGH/True") #high is droog
        else:
            print("0/GPIO.LOW/False")
        sleep(1.0)         # wacht 1.0 seconde

except KeyboardInterrupt:
    GPIO.cleanup()
