import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BOARD)
enable1 = 3
enable2 = 11
input1 = 5
input2 = 7
input3 = 8
input4 = 10
GPIO.setup(enable1, GPIO.OUT)
#GPIO.setup(enable2, GPIO.OUT)
GPIO.setup(input1, GPIO.OUT)
GPIO.setup(input2, GPIO.OUT)
#GPIO.setup(input3, GPIO.OUT)
#GPIO.setup(input4, GPIO.OUT)
pwm1 = GPIO.PWM(enable1, 100)
#pwm2 = GPIO.PWM(enable2, 100)
sleep(0.5)
print("waiting")
pwm1.start(0)
#pwm2.start(0)
GPIO.output(input1, False)
GPIO.output(input2, True)
#GPIO.output(input3, False)
#GPIO.output(input4, False)
GPIO.output(enable1, True)
#GPIO.output(enable2, True)
pwm1.ChangeDutyCycle(50)
#pwm2.ChangeDutyCycle(50)
sleep(5)
GPIO.output(enable1, False)
#GPIO.output(enable2, False)
GPIO.cleanup()

