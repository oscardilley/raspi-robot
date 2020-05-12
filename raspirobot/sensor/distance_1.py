import RPi.GPIO as GPIO
from time import sleep
from time import time
GPIO.setmode(GPIO.BOARD)
trigger_1 = 13 #using pi board numbering, select the sensor 1 gpio trigger
echo_1 = 12 #select the echo pin for the input
GPIO.setup(trigger_1, GPIO.OUT)
GPIO.setup(echo_1, GPIO.IN)
GPIO.output(trigger_1, False)
print("Settling sensor 1")
sleep(2)

def distance_1():
  GPIO.output(trigger_1, True)
  sleep(0.00001) #sensor requires a 10us squarewave to begin sensing
  GPIO.output(trigger_1, False)
  pulse_1_start = time() #unsure why these lines are required, test again without
  pulse_1_end = time() # "
  
  while GPIO.input(echo_1)==0:
    pulse_1_start = time()
  while GPIO.input(echo_1)==1:
    pulse_1_end = time()
   
  pulse_duration_1 = pulse_1_end - pulse_1_start
  distance_1 = pulse_duration_1*(34326/2)
  return distance_1

#need to now define a condition to remain true whilst we want to sense
#and find a way to print returned distance to the HMI, add 0.5s sleep
#this will prevent jittery distance, use "%.2f cm"

