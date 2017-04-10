import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print("Socket Created")

host = '127.0.0.1'
port = 1688
s.bind((host,port))
s.listen(5)

conn,addr = s.accept()
print("Client Address:", addr)

while True:
    data = conn.recv(1024)
    if data:
        print("Receive Data:", data.decode('utf-8'))
    else:
        break

conn.close()
