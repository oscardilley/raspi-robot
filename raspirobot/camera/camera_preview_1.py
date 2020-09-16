from picamera import PiCamera
from time import sleep

camera = PiCamera()
camera.start_preview()
sleep(5)
camera.image_effect = "colorswap"
sleep(5)
camera.image_effect = "negative"
sleep(5)
camera.image_effect = "posterise"
sleep(5)
camera.stop_preview()
