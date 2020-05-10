import RPi.GPIO as GPIO
from time import sleep
import time
GPIO.setmode(GPIO.BOARD)
trigger_1 = 12 #using pi board numbering, select the sensor 1 gpio trigger
echo_1 = 13 #select the echo pin for the input
GPIO.setup(trigger_1, GPIO.OUT)
GPIO.setup(echo_1, GPIO.IN)
GPIO.output(trigger_1, False)
print("Settling sensor 1")
sleep(2)

def distance_1():

