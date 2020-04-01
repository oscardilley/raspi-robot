print("Hello, welcome to my robot") #test
from picamera import PiCamera
from picamera import color
from time import sleep

camera = PiCamera()
camera.start_preview()
sleep(5)
camera.stop_preview()
