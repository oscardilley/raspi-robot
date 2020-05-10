import RPi.GPIO as GPIO
from time import sleep
import time
GPIO.setmode(GPIO.BOARD)
trigger_2 = 14 #using pi board numbering, select the sensor 1 gpio trigger
echo_2 = 15 #select the echo pin for the input
GPIO.setup(trigger_2, GPIO.OUT)
GPIO.setup(echo_2, GPIO.IN)
GPIO.output(trigger_2, False)
print("Settling sensor 2")
sleep(2)

def distance_2():
  GPIO.output(trigger_2, True)
  sleep(0.00001) #sensor requires a 10us squarewave to begin sensing
  GPIO.output(trigger_2, False)
  pulse_2_start = time.time() #unsure why these lines are required, test again without
  pulse_2_end = time.time() # "
  
  while GPIO.input(echo_2)==0:
    pulse_2_start = time.time()
  while GPIO.input(echo_2)==1:
    pulse_2_end = time.time()
   
  pulse_duration_2 = pulse_2_end - pulse_2_start
  distance_2 = pulse_duration_2*(34326/2)
  return distance_2
