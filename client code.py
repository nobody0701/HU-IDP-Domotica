import socket
import time as timu
from vochtigheid import Vochtigheid
from infrarood import Infrarood
import RPi.GPIO as GPIO

GPIO.setwarnings(False)    # geen foutmeldinging van de pinnen
GPIO.setmode(GPIO.BCM)     # gebruik nummering achter GPIO op afbeelding
GPIO.setup(14, GPIO.IN)    # Alarmknop
GPIO.setup(15, GPIO.IN)

idaa = str(input('Input ID: '))

def client_program():
    host = socket.gethostname()
    port = 5000

    client_socket = socket.socket()
    try:
        client_socket.connect((host, port))
        print("[Socket] Connected to host: " + str(host) + ' port: ' + str(port))
        client_socket.send(str(idaa).encode())
        timu.sleep(0.5)
        inrood = False
        alarmknop = False
        helpknop = False
        def alarmactie():
            global alarmknop
            print('Alarm')
            alarmknop = True
        def helpactie():
            global helpknop
            print('help')
            helpknop = True
        GPIO.add_event_detect(14, GPIO.BOTH, callback=alarmactie, bouncetime=5000) # noodknop klik button voert chng uit
        GPIO.add_event_detect(15, GPIO.BOTH, callback=helpactie, bouncetime=5000)
        while True:
            datadict = {}
            if helpknop:
                datadict.update({'help': ('melding', 'help')})
                helpknop = False
            if alarmknop:
                datadict.update({'alarm': ('melding', 'alarm')})
                alarmknop = False
            vocht = Vochtigheid()
            if vocht:
                datadict.update({'vochtig': ('melding', 'nat')})
            infrood = Infrarood(inrood)
            if infrood:
                datadict.update({'infrarood': ('melding', 'beweging')})
            client_socket.send(str(datadict).encode())
            ontvangendata = client_socket.recv(128).decode()
            ontvangendata = eval(ontvangendata)
            if ontvangendata['infrarood']:
                inrood = True
            else:
                inrood = False
            print(ontvangendata)
            timu.sleep(0.08)
    except ConnectionResetError:
        print('[Socket] De verbinding is verloren met de doelcomputer')
        input('[Socket] Druk op enter om het opnieuw te proberen')
        client_program()
    except ConnectionRefusedError:
        print('[Socket] Kan geen verbinding maken met de doelcomputer')
        input('[Socket] Druk op enter om het opnieuw te proberen')
        client_program()

if __name__ == '__main__':
    client_program()
