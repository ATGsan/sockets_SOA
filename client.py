import socket
import sys

s = socket.socket()
s.connect((sys.argv[1], 8080))
s.send(bytes(sys.argv[2], encoding='utf-8'))

data = s.recv(1024)
s.close()

print(data)

