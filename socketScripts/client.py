'''
import socket

BUFFER = 1024
PORT = 5050

my_socket = socket.socket()
my_socket.connect(('10.50.115.95', PORT))

my_socket.send(bytes('Hello from client', encoding="utf8"))
response = my_socket.recv(BUFFER)

print(response)
my_socket.close()
'''
import socket
import pickle

HEADERSIZE = 10
ADDRESS = socket.gethostbyname(socket.gethostname())
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((ADDRESS, 1243))

while True:
    full_msg = b''
    new_msg = True
    while True:
        msg = s.recv(16)
        if new_msg:
            # print("new msg len:", msg[:HEADERSIZE])
            msglen = int(msg[:HEADERSIZE])
            new_msg = False

        full_msg += msg

        if len(full_msg)-HEADERSIZE == msglen:
            # print("full msg recvd")
            # print(full_msg[HEADERSIZE:])
            d = pickle.loads(full_msg[HEADERSIZE:])
            print(d)
            new_msg = True
            full_msg = b''
