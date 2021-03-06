import RPi.GPIO as gpio
from time import sleep, time

class Distance_Sensor():

  def __init__(self):
    self.trigger = 13
    self.echo = 12
    gpio.setmode(gpio.BOARD)
    gpio.setup(self.trigger, gpio.OUT)
    gpio.setup(self.echo, gpio.IN)
    gpio.output(self.trigger, False)

  def distance_function(self):
    pulse_start = time()
    pulse_end = time()
    gpio.output(self.trigger, True)
    sleep(0.000015)
    gpio.output(self.trigger, False)
    while gpio.input(self.echo) == 0:
      pulse_start = time()
    while gpio.input(self.echo) == 1:
      pulse_end = time()
    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration*(34326/2)
    return distance
 
  def returning_distance(self):
    while True:
        sleep(1)
        print("%.2f cm" % self.distance_function())
    
test = Distance_Sensor()
test.returning_distance()


