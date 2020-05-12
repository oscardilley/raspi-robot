#-------------------------------------------------------------------------------------------------------------------------
# This program is run from __main__ on run of this repository and this file functions as main centre to run this project.
# This will be responsible for all the necessary imports of the camera, sensors and motor software to run the robot.
# It will also initalise the GUI
# This should be clearly organised and simple, calling functions without much other code.
#-------------------------------------------------------------------------------------------------------------------------

from time import sleep
#boot up initial functionality and rest for a second or two
print("Initialising robot...")
sleep(2)

#import distance functions, find a way to use a function to calculate the average value using def distance_average(1, 2):

from sensor.distance_1 import distance_1

#boot up initial functionality and rest for a second or two
while True:
  dist = distance_1()
  print("Distance = %.2f" %dist)
  sleep(0.5)
#import forwards, backwards, left, right functions

#run camera function

#link camera display/ preview function to a show camera button on centre of GUI

#change view button on GUI cycles through desired PI camera effects

#use a text.repeat(500, distance_average) to call the distance into GUI every 0.5s

#take an input value from slider 0-100 for %PWM speed and input that into all direction functions

#link the direction functions to the buttons, on when held

#make buttons exclusive to press if possible

#final GUI.display()

