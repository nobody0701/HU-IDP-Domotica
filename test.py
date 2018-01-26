import RPi.GPIO as GPIO
import Adafruit_DHT
import socket
import time
import datetime
import threading
GPIO.setwarnings(False)    # geen foutmeldinging van de pinnen
GPIO.setmode(GPIO.BCM)     # gebruik nummering achter GPIO op afbeelding
GPIO.setup(25, GPIO.IN)    # adafruit
GPIO.setup(14, GPIO.IN)    # Alarmknop
GPIO.setup(15, GPIO.IN)    # hulpknop

#info = dict(statusHulp=False, statusAlarm=False, temp=0)

def noodknp(channel):
    print("WIE-YOE-WIE-YOE")
    UDP_IP = "192.168.2.8"
    UDP_PORT = 5005
    data = "Alarm aan"
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.sendto(data, (UDP_IP, UDP_PORT))

def chng(channel):
    print("geef hulp dan")

def reveice_message():
    UDP_IP = "192.168.2.8"
    UDP_PORT = 5005
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((UDP_IP, UDP_PORT))
    while True:
        data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
        print("received message:", data)
        if data:
            return data

GPIO.add_event_detect(14, GPIO.BOTH, callback=noodknp, bouncetime=5000) # noodknop klik button voert chng uit
GPIO.add_event_detect(15, GPIO.BOTH, callback=chng, bouncetime=5000) # hulpknop klik button voert chng uit

vochtigheid, temperatuur = Adafruit_DHT.read_retry(Adafruit_DHT.DHT11, 25)
temper = temperatuur
vochtig = vochtigheid

try:
    while True:
        def led_aan():
          print("RIJ STOFZUIGER RIJ")

        print(temper, vochtig)

        day_of_week = datetime.date.today().weekday() # 0 is Monday, 6 is Sunday
        time = datetime.datetime.now().time()


        if (time > datetime.time(23,01) and time < datetime.time(23,03)): #stofzuiger timer
          led_aan()

        t1 = threading.Thread(target=reveice_message)
        t1.start()
        t1.join()

except KeyboardInterrupt:
    GPIO.cleanup()

