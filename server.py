import socket

hostname = socket.gethostname()
local_ip = socket.gethostbyname(hostname)

print(local_ip, flush=True)

s = socket.socket()
s.bind(('', 8080))
s.listen(1)
while True:
    try:
        conn, addr = s.accept()


        while True:
            data = conn.recv(1024)
            if not data:
                break
            print(data, flush=True)
            conn.send(data[::-1])
    except KeyboardInterrupt:
        print("STOPING")
        break
conn.close()
