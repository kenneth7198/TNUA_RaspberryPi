import socket
import picamera

camera = picamera.PiCamera()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

print("Socket Created")

host = '192.168.3.4'
port = 1688

s.bind((host,port))
s.listen(5)

conn,addr = s.accept()
print("Client Address: %s" % str(addr))

while True:
    data = conn.recv(1024)
    if data:
        print("Receive Data: %s" % str(data.decode('utf-8')))
        recvData = str(data.decode('utf-8'))
        if recvData == "ON":
            print("snapshot")
            camera.capture('img.jpg')
            camera.start_preview()
        else:
            print("preview off")
            camera.stop_preview()
    else:
        break

conn.close()
