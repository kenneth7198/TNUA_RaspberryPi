import time
import wiringpi

servoPin = 21

wiringpi.wiringPiSetupGpio()
wiringpi.pinMode(servoPin, wiringpi.GPIO.PWM_OUTPUT)
wiringpi.pwmSetMode(wiringpi.GPIO.PWM_MODE_MS)
wiringpi.pwmSetClock(192)
wiringpi.pwmSetRange(2000)

delay_period = 0.01

while True:
    for pulse in range(50,250,1):
        wiringpi.pwmWrite(servoPin, pulse)
        time.sleep(delay_period)
    for pulse in range(250, 50, -1):
        wiringpi.pwmWrite(servoPin, pulse)
        time.sleep(delay_period)
