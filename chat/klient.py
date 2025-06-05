
import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(("192.168.222.236", 65231))

try:
    message = "start"
    client_socket.send(message.encode())
    response = client_socket.recv(1024)
    print(f"Odpověď od serveru: {response.decode()}")
    message = "velikost OK"
    client_socket.send(message.encode())
    while True:
        tah = client_socket.recv(1024)
        if tah.decode()!="":
            print(f"Odpověď od serveru: {tah.decode()}")
            break

finally:

    client_socket.close()