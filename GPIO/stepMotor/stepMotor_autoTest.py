import RPi.GPIO as GPIO
import time

inA=13
inB=12
inC=11
inD=10

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(inA, GPIO.OUT)
GPIO.setup(inB, GPIO.OUT)
GPIO.setup(inC, GPIO.OUT)
GPIO.setup(inD, GPIO.OUT)

def setStep(w1, w2, w3, w4):
    GPIO.output(inA, w1)
    GPIO.output(inB, w2)
    GPIO.output(inC, w3)
    GPIO.output(inD, w4)

def forward(delay, steps):
    for i in range(0, steps):
        setStep(0,0,1,1)
        time.sleep(delay)
        setStep(1,0,0,1)
        time.sleep(delay)
        setStep(1,1,0,0)
        time.sleep(delay)
        setStep(0,1,1,0)
        time.sleep(delay)

def backward(delay, steps):
    for i in range(0, steps):
        setStep(0,1,1,0)
        time.sleep(delay)
        setStep(1,1,0,0)
        time.sleep(delay)
        setStep(1,0,0,1)
        time.sleep(delay)
        setStep(0,0,1,1)
        time.sleep(delay)

while True:
    #delay = raw_input("Please input delay time:")
    steps = raw_input("How many steps forward?")
    forward(int(5) / 1000.0, int(512))
    steps = raw_input("How many steps backward?")
    backward(int(5) / 1000.0, int(512))
    #setStep(0,0,0,0)
    
