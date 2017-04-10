import socket
import time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print("Socket Created")

host = '192.168.3.4'
port = 1688
s.connect((host,port))

while True:
    data = s.recv(1024)
    print(data.decode('utf-8'))
    
s.close()
