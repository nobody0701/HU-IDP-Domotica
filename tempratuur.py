import RPi.GPIO as GPIO
import Adafruit_DHT
import time
import datetime
GPIO.setwarnings(False)    #geen foutmeldinging van de pinnen
GPIO.setmode(GPIO.BCM)     # gebruik nummering achter GPIO op afbeelding
GPIO.setup(25, GPIO.IN)    # Hulpknop
GPIO.setup(14, GPIO.IN)    # Alarmknop
GPIO.setup(15, GPIO.IN)    # open

info = dict(statusHulp=False, statusAlarm=False, temp=0)

def chng(channel):
    print("de waarde van ")

GPIO.add_event_detect(14, GPIO.RISING, callback=chng, bouncetime=3) #klik button voert chng uit
try:
    while True:
        vochtigheid, temperatuur = Adafruit_DHT.read_retry(Adafruit_DHT.DHT11, 25)
        temperatuur = round(temperature, 2)
        if resultaat.is_valid():
            info.update(dict(temp=resultaat.temperature))


        print(info)
        if GPIO.input(25): # if port 25 == 1 #vochtsensor
            info.update(dict(statusHulp=True))
            print(info)
            time.sleep(2.0)
        else:
            print("0/GPIO.LOW/False")
            time.sleep(1.0)         # wacht 1.0 seconde

#        if GPIO.input(14): # if port 25 == 1
#            print("1") #toestand wel ingedrukt
#        else:
#            print("0") #toestand niet ingedrukt
#        sleep(1.0)         # wacht 1.0 seconde

        if GPIO.input(15):
            print("aan")    #wel ingedrukt
        else:
            print("uit")


except KeyboardInterrupt:
    GPIO.cleanup()
