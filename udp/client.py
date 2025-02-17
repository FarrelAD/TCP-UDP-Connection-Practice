# SIMPLE IMPLEMENTATION OF UDP CONNECTION
# CLIENT

import socket

HOST = '127.0.0.1'
PORT = 8001

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

try:
    while True:
        user_input = input('Send message: ')
        client_socket.sendto(user_input.encode(), (HOST, PORT))

        data, server_address = client_socket.recvfrom(1024)
        print(f'Server response: {data.decode()}')
finally:
    client_socket.close()