# SIMPLE IMPLEMENTATION OF TCP CONNECTION
# SERVER

import socket

HOST = '127.0.0.1'
PORT = 8000

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen()

print(f'TCP server listening on {HOST}:{PORT}')

while True:
    client_socket, client_address = server_socket.accept()
    
    print(f'Connection from {client_address}')
    
    data = client_socket.recv(1024).decode()
    print(f'Received: {data}')
    
    client_socket.sendall("Hello from server!".encode())
    
    client_socket.close()