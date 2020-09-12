# this file is setup to test the functionality of my distance sensing program and to experiment with how to read off the distance

from . import sensor
from sensor import distance_1

while True:
  distance = distance_1()
  print("Distance = %.2f" %distance)
  sleep(0.5)
