import time
import RPi.GPIO as GPIO
from enum import Enum

def delay(ms):
    time.sleep(ms*0.001)

class Port(Enum):
    A = [16, 15]
    B = [23, 26]
    C = 3
    D = 4	

class Sensor:
    port = None
    
    def __init__(self, port):
        self.port = port	

class TouchSensor(Sensor):
    
    def isPressed():
        return true

class LightSensor(Sensor):
    
    def getValue():
        return 0.01
		
class TouchSensor(Sensor):
    
    def isPressed():
        return true
		
class Motor:
    
    port = None
    speed = 50
    
    def __init__(self, port):
        assert isinstance(port, Port)
        self._setupPins(port)
        self.port = port;
    
    def _setupPins(port):
        GPIO.cleanup()
        GPIO.setmode(GPIO.BOARD)       
        GPIO.setup(port.value[0], GPIO.OUT)    
        GPIO.setup(port.value[1], GPIO.OUT)
        pin1 = GPIO.PWM(port.value[0], self.speed) // frequency 50HZ by default for both pins
        pin2 = GPIO.PWM(port.value[1], self.speed)
        pin1.ChangeDutyCycle(self.speed)
        pin2.ChangeDutyCycle(self.speed)
    
    def forward(self):
        GPIO.output(self.port.value[1], GPIO.LOW)
        time.sleep(0.01)
        GPIO.output(self.port.value[0], GPIO.HIGH)
        time.sleep(0.01)
        
    def backwards(self):
        GPIO.output(self.port.value[0], GPIO.LOW)
        time.sleep(0.01)
        GPIO.output(self.port.value[1], GPIO.HIGH)
        time.sleep(0.01)
        
    def stop(self):
        GPIO.output(self.port.value[0], GPIO.LOW)
        time.sleep(0.01)
        GPIO.output(self.port.value[1], GPIO.LOW)
        time.sleep(0.01)
        
    def setSpeed(self, speed):
        self.speed = speed
        
    def getSpeed(self):
        return self.speed