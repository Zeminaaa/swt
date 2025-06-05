import socket
import json
 
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("0.0.0.0", 65231))
server_socket.listen(5)
print("Server běží, čeká na připojení...")
 
while True:
    client_socket, client_address = server_socket.accept()
    print(f"Připojení od {client_address}")
   
    velikost = "size:10"
    souradnice = [15,5]
 
 
    try:
        data = client_socket.recv(1024)
        print(f"Přijato: {data.decode()}")
        client_socket.send(json.dumps(souradnice).encode())
        data = client_socket.recv(1024)
        print(f"Přijato: {data.decode()}")
        client_socket.send("tah:15,15".encode())
 
    finally:
        client_socket.close()
 