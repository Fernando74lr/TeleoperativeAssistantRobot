import socket

PORT = 5050  # socket.gethostbyname(socket.gethostname())
NUM_REQUESTS = 5
BUFFER = 1024

my_socket = socket.socket()
my_socket.bind(('10.50.115.95', PORT))
my_socket.listen(NUM_REQUESTS)

while(True):
    conn, addr = my_socket.accept()
    print('New connection established!')
    print(addr)

    req = conn.recv(BUFFER)
    print(req)
    conn.send(bytes('Hello world!', encoding="utf8"))
    conn.close()
