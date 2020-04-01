print("Hello, welcome to my robot") #test
form picamera import PiCamera
from picamera import color
from time import sleep

camera = PiCamera()
camera.start_preview()
sleep(5)
camera.stop_preview()
