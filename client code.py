import socket
import time

def client_program():
    host = socket.gethostname()
    port = 5000

    client_socket = socket.socket()
    try:
        client_socket.connect((host, port))
        print("[Socket] Connected to host: " + str(host) + ' port: ' + str(port))
        data = 0
        while True:
            client_socket.send(str(data).encode())
            data = client_socket.recv(1024).decode()
            #time.sleep(0.5)
            print(data)
            data = int(data) + 1
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
