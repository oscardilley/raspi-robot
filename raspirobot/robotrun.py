#-------------------------------------------------------------------------------------------------------------------------
# This program is run from __main__ on run of this repository and this file functions as main centre to run this project.
# This will be responsible for all the necessary imports of the camera, sensors and motor software to run the robot.
# It will also initalise the GUI
# This should be clearly organised and simple, calling functions without much other code.
# gui program should manage most of the mess, camera function should allow for changing display
# gui needs to return button press information and pwm slider information
# gui must have button exlcusivity
# use a text.repeat(500, distance_average) to call the distance into GUI every 0.5s

# 1. run import statements
# 2. call average distance function
# 3. call camera
# 4. call gui

#-------------------------------------------------------------------------------------------------------------------------

from time import sleep
from raspirobot.sensor.distance_1 import distance_1
from raspirobot.GUI.GUI_2 import gui_2

print("hello")

while True:
  dist = distance_1()
  print("Distance = %.2f" %dist)
  sleep(1)

gui_2()
