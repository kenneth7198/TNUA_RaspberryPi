import socket
import time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

print("Socket Created")

host = '192.168.3.4'
port = 1688

s.bind((host,port))
s.listen(5)

conn,addr = s.accept()
print("Client Address: %s" % str(addr))
counter = 0
while True:
    data = "I'm Rpi:" + str(counter)
    conn.send(data.encode('utf-8'))
    time.sleep(1)
    counter += 1

conn.close()
