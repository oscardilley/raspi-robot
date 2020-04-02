import RPi.GPIO as GPIO
from time import sleep
import time
GPIO.setmode(GPIO.BOARD)
trig = 13
echo = 12
GPIO.setup(trig, GPIO.OUT)
GPIO.setup(echo, GPIO.IN)
GPIO.output(trig, False)
sleep(2)

def distance():
    GPIO.output(trig, True)
    sleep(0.00001)
    GPIO.output(trig, False)
    pulse_start = time.time()
    pulse_end = time.time()
    
    while GPIO.input(echo) ==0:
        pulse_start = time.time()
    while GPIO.input(echo) ==1:
        pulse_end = time.time()
    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration*(34326/2)
    return distance

while True:
    dist = distance()
    print("Distance = %.2f cm" %dist)
    sleep(0.5)
