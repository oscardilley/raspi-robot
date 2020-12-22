from time import sleep
import RPi.gpio as gpio

gpio.setmode(gpio.BOARD)
gpio.clearup()
enable1 = 3
enable2 = 11
input1 = 5
input2 = 7
input3 = 8
input4 = 10
gpio.setup(enable1, gpio.OUT)
gpio.setup(enable2, gpio.OUT)
gpio.setup(input1, gpio.OUT)
gpio.setup(input2, gpio.OUT)
gpio.setup(input3, gpio.OUT)
gpio.setup(input4, gpio.OUT)
pwm1 = gpio.PWM(enable1, 100)
pwm2 = gpio.PWM(enable2, 100)

def forward_move():
