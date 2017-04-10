import serial

port = "/dev/ttyUSB0"
arduino = serial.Serial(port, 9600)
arduino.flushInput()

while True:
    if(arduino.inWaiting() > 0):
        input = arduino.read(1)
        print(ord(input))
