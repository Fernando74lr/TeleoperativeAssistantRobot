import socket

BUFFER = 1024
PORT = 5050

my_socket = socket.socket()
my_socket.connect(('10.50.115.95', PORT))

my_socket.send(bytes('Hello from client', encoding="utf8"))
response = my_socket.recv(BUFFER)

print(response)
my_socket.close()
