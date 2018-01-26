import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)     # gebruik nummering achter GPIO op afbeelding
#GPIO.setup(25, GPIO.IN)    # nummer 25 als input, vocht = LOW
GPIO.setup(14, GPIO.IN)
GPIO.setup(15, GPIO.IN)


def chng(channel):
    print("de waarde van ")

GPIO.add_event_detect(14, GPIO.RISING, callback=chng, bouncetime=3) #klik button voert chng uit
try:
    while True:
        if GPIO.input(15):
            print("aan")    #wel ingedrukt
        else:
            print("uit")
except KeyboardInterrupt:
    GPIO.cleanup()

def noodknp(channel):
    print("WIE-YOE-WIE-YOE")
    UDP_IP = "192.168.2.8"
    UDP_PORT = 5005
    data = "Alarm aan"
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto(data, (UDP_IP, UDP_PORT))
