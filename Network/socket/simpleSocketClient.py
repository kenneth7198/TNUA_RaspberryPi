import socket
import time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print("Socket Created")

host = '192.168.3.4'
port = 1688
s.connect((host,port))

counter = 0

while True:
    data = "Hello Pi!:" + str(counter) 
    s.sendall(data.encode('utf-8'))
    print("Send data to server")
    time.sleep(1)
    counter += 1
    
s.close()
ก็
