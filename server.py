'''
import socket

PORT = 5050  # socket.gethostbyname(socket.gethostname())
NUM_REQUESTS = 10
BUFFER = 1024
ADDRESS = socket.gethostbyname(socket.gethostname())

print(ADDRESS)

my_socket = socket.socket()
my_socket.bind((ADDRESS, PORT))
my_socket.listen(NUM_REQUESTS)

while(True):
    conn, addr = my_socket.accept()
    print('New connection established!')
    print(addr)

    req = conn.recv(BUFFER)
    print(req)
    conn.send(bytes('Hello world!', encoding="utf8"))
    conn.close()

'''
import socket
import time
# 172.19.16.1

HEADERSIZE = 10
ADDRESS = socket.gethostbyname(socket.gethostname())

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((ADDRESS, 1243))
print(ADDRESS)
s.listen(5)

while True:
    # now our endpoint knows about the OTHER endpoint.
    clientsocket, address = s.accept()
    print(f"Connection from {address} has been established.")

    msg = "Welcome to the server!"
    msg = f"{len(msg):<{HEADERSIZE}}"+msg

    clientsocket.send(bytes(msg, "utf-8"))

    while True:
        time.sleep(1)
        msg = f"The time is {time.time()}"
        msg = f"{len(msg):<{HEADERSIZE}}"+msg

        print(msg)

        clientsocket.send(bytes(msg, "utf-8"))
