import socket
import time
# import pickle

HEADERSIZE = 20
ADDRESS = '172.25.176.1'#socket.gethostbyname(socket.gethostname())
'    fist'

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((ADDRESS, 1243))
print(ADDRESS)
s.listen(5)


# def server(msg):
#     # while True:
#     clientsocket, address = s.accept()
#     print(f"Connection from {address} has been established.")

#     while True:
#         time.sleep(2)
#         clientsocket.send(msg)

while True:
    clientsocket, address = s.accept()
    print(f"Connection from {address} has been established.")

    while True:
        time.sleep(1)
        clientsocket.sendall(bytes('esta es una prueba', 'utf-8'))

'''
d = {1: 'Hey', 2: 'There'}
msg = pickle.dumps(d)
msg = bytes(f'{len(msg):<{HEADERSIZE}}', 'utf-8') + msg
'''
