from time import sleep
import RPi.GPIO as gpio


class RaspiMotion():
  
  
  def __init__(self):
    gpio.setmode(gpio.BOARD)
    self.en1 = 3
    self.en2 = 11
    self.in1 = 5
    self.in2 = 7
    self.in3 = 8
    self.in4 = 10
    gpio.setup(en1, gpio.OUT)
    gpio.setup(en2, gpio.OUT)
    gpio.setup(in1, gpio.OUT)
    gpio.setup(in2, gpio.OUT)
    gpio.setup(in3, gpio.OUT)
    gpio.setup(in4, gpio.OUT)
    pwm1 = gpio.PWM(en1, 100)
    pwm2 = gpio.PWM(en2, 100)
    
    
  def forward_move(self):
    gpio.output(self.in1 , False)
    gpio.output(self.in2 , True)
    gpio.output(self.in3 , True)
    gpio.output(self.in4 , False)
    self.pwm1.ChangeDutyCycle(50)
    self.pwm2.ChangeDutyCycle(50) 
    gpio.output(self.en1, True)
    gpio.output(self.en2, True)
    sleep(5)
    gpio.output(self.en1, False)
    gpio.output(self.en2, False)
  
test = RaspiMotion()
test.forward_move()
