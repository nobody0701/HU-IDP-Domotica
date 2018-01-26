import socket
import time as timu

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
        while True:
            data = {1: ('melding', 'alarm'), 2: ('melding', 'napa')}
            client_socket.send(str(data).encode())
            ontvangendata = client_socket.recv(128).decode()
            ontvangendata = eval(ontvangendata)
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
