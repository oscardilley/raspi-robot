from picamera import PiCamera
from time import sleep

camera = PiCamera()
camera.start_preview()
camera. resolution = (960, 540)
sleep(5)
# camera.image_effect = "colorswap"
# camera.image_effect = "negative"
# camera.image_effect = "posterise"
camera.stop_preview()
