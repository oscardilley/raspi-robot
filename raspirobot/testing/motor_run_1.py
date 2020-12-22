import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BOARD)
# GPIO.clearup()
enable1 = 3
enable2 = 11
input1 = 5
input2 = 7
input3 = 8
input4 = 10
GPIO.setup(enable1, GPIO.OUT)
GPIO.setup(enable2, GPIO.OUT)
GPIO.setup(input1, GPIO.OUT)
GPIO.setup(input2, GPIO.OUT)
GPIO.setup(input3, GPIO.OUT)
GPIO.setup(input4, GPIO.OUT)
pwm1 = GPIO.PWM(enable1, 100)
pwm2 = GPIO.PWM(enable2, 100)

pwm1.ChangeDutyCycle(50)
pwm2.ChangeDutyCycle(50)
GPIO.output(input1, True)
GPIO.output(input2, False)
GPIO.output(input3, True)
GPIO.output(input4, False)


