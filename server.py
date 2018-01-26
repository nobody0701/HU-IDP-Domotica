import socket
import RPi.GPIO as GPIO
import time

def recivie_data():
   UDP_IP = "192.168.137.180"
   UDP_PORT = 5005
   sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
   sock.bind((UDP_IP, UDP_PORT))
   while True:
        data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
        print("received message:", data)
        if data:
            return data
def controle():
   UDP_IP = "192.168.137.15"
   UDP_PORT = 500
   data = "connect"
   sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
   sock.sendto(data, (UDP_IP, UDP_PORT))

LedG = 29
LedR = 31
speaker = 33
Switch = 36

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(LedG, GPIO.OUT)
GPIO.setup(LedR, GPIO.OUT)
GPIO.setup(speaker, GPIO.OUT)
GPIO.setup(Switch, GPIO.OUT)

GPIO.output(LedG, True)

alarm_time = time.time()
alarm_on = False

try:
    while True:
        data = recivie_data()

        if data == "Alarm aan":
            while True:
                # Elke 1 seconde
                if (time.time() - alarm_time >= 1):
                    alarm_time = time.time()
                    alarm_on = not alarm_on


                if GPIO.input(Switch):
                    #print("Alarm uit")
                    GPIO.output(LedG, True)
                    GPIO.output(LedR, False)
                    GPIO.output(speaker, False)
                    print("uit")
                    #data = ""
                    # TODO stuur naar client dat die uit mag



                GPIO.output(LedR, alarm_on)
                GPIO.output(speaker, alarm_on)
                GPIO.output(LedG, False)
                break
##                print("Alarm aan")
        elif data == "uit":
            while True:
                print("Alarm uit")
                GPIO.output(LedG, True)
                GPIO.output(LedR, False)
                GPIO.output(speaker, False)
                break
        elif

        time.sleep(1)

except KeyboardInterrupt:
   GPIO.cleanup()
