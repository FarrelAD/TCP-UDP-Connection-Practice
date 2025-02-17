# SIMPLE IMPLEMENTATION OF UDP CONNECTION
# SERVER

import socket

HOST = '127.0.0.1'
PORT = 8001

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind((HOST, PORT))

print(f'UDP server listening on {HOST}:{PORT}')

while True:
    data, client_address = server_socket.recvfrom(1024)
    print(f'Received data from {client_address}: {data.decode()}')
    
    server_socket.sendto("Hello I'm a UDP server !".encode(), client_address)
