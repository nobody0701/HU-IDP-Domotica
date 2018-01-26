import socket
import time as timu
from status import lezenstatus, Status, verbindingverloren

def server_program():
    host = socket.gethostname()
    port = 5000
    server_socket = socket.socket()
    server_socket.bind((host, port))
    server_socket.listen(1)
    print("[Socket] host: " + str(host) + ' port: ' + str(port))
    try:
        conn, address = server_socket.accept()
        idaa = conn.recv(128).decode()
        print("Connection from: " + str(address) + " with id: " + str(idaa))
        while True:
            data = conn.recv(1024).decode()
            if data:
                print(data)
                lezenstatus(data, idaa)
                timu.sleep(0.08)
                datasend = Status(idaa)
                conn.send(str(datasend).encode())
            else:
                print('Fout')
    except ConnectionResetError:
        server_socket.close()
        print('[Socket] De verbinding is verloren.')
        verbindingverloren(idaa)
        server_program()

if __name__ == '__main__':
    server_program()
