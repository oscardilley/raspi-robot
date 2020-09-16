from picamera import PiCamera
from time import sleep

camera = PiCamera()
camera.start_preview()
camera. resolution = (500, 300)
sleep(5)
# camera.image_effect = "colorswap"
# camera.image_effect = "negative"
# camera.image_effect = "posterise"
camera.stop_preview()
