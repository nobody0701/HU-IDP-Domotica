import RPi.GPIO as GPIO
import time
import socket
GPIO.setmode(GPIO.BOARD)

sensor = 12
led = 11
knop = 36
knoprun = 38

GPIO.setwarnings(False)
GPIO.setup(sensor, GPIO.IN, GPIO.PUD_UP)
GPIO.setup(led, GPIO.OUT)
GPIO.setup(knop, GPIO.IN)
GPIO.setup(knoprun, GPIO.IN)

def alarmOn():
    UDP_IP = "192.168.137.235"
    UDP_PORT = 5005
    data = "Alarm aan"
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto(data, (UDP_IP, UDP_PORT))

def alarmOFF():
    UDP_IP = "192.168.137.235"
    UDP_PORT = 5005
    data = "uit"
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto(data, (UDP_IP, UDP_PORT))
def client():
    x = time.sleep(10)
    while True:
        i = GPIO.input(sensor)
        j= GPIO.input(knop)
        if i == 1:
            x
            alarmOn()
            GPIO.output(led, True)
            print("aan")
            x = time.sleep(0)
            time.sleep(2)
        if j == 1 :
            alarmOFF()
            print('knop')
            break
while True:
    p = GPIO.input(knoprun)
    if p == 1:
        client()







