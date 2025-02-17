# SIMPLE IMPLEMENTATION OF TCP CONNECTION
# CLIENT

import socket

HOST = '127.0.0.1'
PORT = 8000

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.connect((HOST, PORT))

while True:
    user_input = input('Send message: ')
    client_socket.sendall(user_input.encode())

    response = client_socket.recv(1024).decode()
    print(f'Response data: {response}')

    client_socket.close()