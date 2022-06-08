from encodings import utf_8
import socket
# import pickle

# HEADERSIZE = 10
ADDRESS = '172.25.176.1' #socket.gethostbyname(socket.gethostname())
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((ADDRESS, 1243))

while True:
    # full_msg = b''
    # new_msg = True
    while True:
        msg = s.recv(1024)
        print(msg.decode('utf_8'))
        # if new_msg:
        #     # print("new msg len:", msg[:HEADERSIZE])
        #     msglen = int(msg[:HEADERSIZE])
        #     new_msg = False

        # full_msg += msg

        # if len(full_msg)-HEADERSIZE == msglen:
        #     d = pickle.loads(full_msg[HEADERSIZE:])
        #     print(d)
        #     new_msg = True
        #     full_msg = b''
