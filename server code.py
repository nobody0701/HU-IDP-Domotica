import socket
import time

def server_program():
    host = socket.gethostname()
    port = 5000
    server_socket = socket.socket()
    server_socket.bind((host, port))
    server_socket.listen(1)
    print("[Socket] host: " + str(host) + ' port: ' + str(port))
    try:
        conn, address = server_socket.accept()
        print("Connection from: " + str(address))

        while True:
            data = conn.recv(1024).decode()
            if data:
                #time.sleep(0.5)
                print(data)
                data = int(data) + 1
                data = Data()
                conn.send(str(data).encode())
            else:
                print('Fout')
    except ConnectionResetError:
        server_socket.close()
        print('[Socket] De verbinding is verloren.')
        server_program()

if __name__ == '__main__':
    server_program()
