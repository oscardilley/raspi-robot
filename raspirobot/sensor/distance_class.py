import RPi.GPIO as gpio
from time import sleep, time

class Distance_Sensor():

  def __init__(self):
    self.trigger = 13
    self.echo = 12
    gpio.setmode(gpio.BOARD)
    gpio.setup(self.trigger, gpio.OUT)
    gpio.setup(self.echo, gpio.IN)
    GPIO.output(self.trigger, False)
  
  def distance_function(self):
    GPIO.output(self.trigger, True)
    sleep(0.00001)
    GPIO.output(self.trigger, False)
    pulse_start = time()
    pulse_end = time()
    while gpio.input(self.echo) == 0:
      pulse_start = time()
    while gpio.input(self.echo) == 1:
      pulse_end = time()
    pulse_duration = pulse_end - pulse_end
    distance = pulse_duration*(34326/2)
    return distance
 
  def returning_distance(self):
    while True:
        sleep(1)
        print(self.distance_function())
    
test = Distance_Sensor()
test.returning_distance()


