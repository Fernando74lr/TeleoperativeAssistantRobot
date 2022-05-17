import socket
import time
# import pickle

HEADERSIZE = 20
ADDRESS = socket.gethostbyname(socket.gethostname())

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((ADDRESS, 1243))
print(ADDRESS)
s.listen(5)


def server(msg):
    # while True:
    clientsocket, address = s.accept()
    print(f"Connection from {address} has been established.")

    while True:
        time.sleep(2)
        clientsocket.send(msg)


'''
d = {1: 'Hey', 2: 'There'}
msg = pickle.dumps(d)
msg = bytes(f'{len(msg):<{HEADERSIZE}}', 'utf-8') + msg
'''
