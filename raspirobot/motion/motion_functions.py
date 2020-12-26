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
    gpio.setup(self.en1, gpio.OUT)
    gpio.setup(self.en2, gpio.OUT)
    gpio.setup(self.in1, gpio.OUT)
    gpio.setup(self.in2, gpio.OUT)
    gpio.setup(self.in3, gpio.OUT)
    gpio.setup(self.in4, gpio.OUT)
    self.pwm1 = gpio.PWM(self.en1, 100)
    self.pwm2 = gpio.PWM(self.en2, 100)
    
  def forward_move(self, length):
    self.pwm1.start(0)
    self.pwm2.start(0)
    gpio.output(self.in1 , False)
    gpio.output(self.in2 , True)
    gpio.output(self.in3 , True)
    gpio.output(self.in4 , False)
    self.pwm1.ChangeDutyCycle(75)
    self.pwm2.ChangeDutyCycle(75) 
    gpio.output(self.en1, True)
    gpio.output(self.en2, True)
    sleep(int(length))
    gpio.output(self.en1, False)
    gpio.output(self.en2, False)
    gpio.output(self.in1 , False)
    gpio.output(self.in2 , False)
    gpio.output(self.in3 , False)
    gpio.output(self.in4 , False)
  
  def backward_move(self, length):
    self.pwm1.start(0)
    self.pwm2.start(0)
    gpio.output(self.in1 , True)
    gpio.output(self.in2 , False)
    gpio.output(self.in3 , False)
    gpio.output(self.in4 , True)
    self.pwm1.ChangeDutyCycle(50)
    self.pwm2.ChangeDutyCycle(50) 
    gpio.output(self.en1, True)
    gpio.output(self.en2, True)
    sleep(int(length))
    gpio.output(self.en1, False)
    gpio.output(self.en2, False)
    gpio.output(self.in1 , False)
    gpio.output(self.in2 , False)
    gpio.output(self.in3 , False)
    gpio.output(self.in4 , False)
   
  def right_move(self, length):
    self.pwm1.start(0)
    self.pwm2.start(0)
    gpio.output(self.in1 , True)
    gpio.output(self.in2 , False)
    gpio.output(self.in3 , True)
    gpio.output(self.in4 , False)
    self.pwm1.ChangeDutyCycle(25)
    self.pwm2.ChangeDutyCycle(100) 
    gpio.output(self.en1, True)
    gpio.output(self.en2, True)
    sleep(int(length))
    gpio.output(self.en1, False)
    gpio.output(self.en2, False)
    gpio.output(self.in1 , False)
    gpio.output(self.in2 , False)
    gpio.output(self.in3 , False)
    gpio.output(self.in4 , False)
    
  def left_move(self, length):
    self.pwm1.start(0)
    self.pwm2.start(0)
    gpio.output(self.in1 , False)
    gpio.output(self.in2 , True)
    gpio.output(self.in3 , False)
    gpio.output(self.in4 , True)
    self.pwm1.ChangeDutyCycle(100)
    self.pwm2.ChangeDutyCycle(25) 
    gpio.output(self.en1, True)
    gpio.output(self.en2, True)
    sleep(int(length))
    gpio.output(self.en1, False)
    gpio.output(self.en2, False)  
    gpio.output(self.in1 , False)
    gpio.output(self.in2 , False)
    gpio.output(self.in3 , False)
    gpio.output(self.in4 , False)
 

