#!/usr/bin/python

import time
import RPi.GPIO as GPIO
import spidev
import time
import os

# ports for motors and sensors
class MotorPort:
    A = [16, 15]
    B = [22, 18]


# global functions 

def delay(ms):
    time.sleep(ms*0.001)

    
# sensors
class Sensor:
    
    _spi = None
    _channel = None
    
    def __init__(self, channel):
        self._validateChannel(channel)        
        self._channel = channel;
        self._openSPIBus()
        
    def _validateChannel(self, channel):
        if(channel > 7 or channel < 0):
            raise ValueError("channel must be a value between 0 and 7")
            
    def _openSPIBus(self):
        self._spi = spidev.SpiDev()
        self._spi.open(0,0)
    
    def _readChannel(self, channel):
        adc = self._spi.xfer2([1,(8+channel)<<4,0])
        data = ((adc[1]&3) << 8) + adc[2]
        return data
    
    def _convertVolts(self, data,places):
        volts = (data * 3.3) / float(1023)
        volts = round(volts,places)
        return volts
    
    def getValue(self):
        level = 1024 - self._readChannel(self._channel)
        #volts = self._convertVolts(level,2)
        return level


class LightSensor(Sensor):
    
    def getValue(self):
        return Sensor.getValue(self)
    
class TouchSensor(Sensor):
    
    def isPressed(self):
        return (Sensor.getValue(self) > 1)
    
# motor
class Motor:
    
    _motorPort = None
    _speed = 50
    _pin1 = None
    _pin2 = None
    
    def __init__(self, motorPort):
        self._motorPort = motorPort;
        self._setupPins()
    
    def _setupPins(self):
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BOARD)       
        GPIO.setup(self._motorPort[0], GPIO.OUT)    
        GPIO.setup(self._motorPort[1], GPIO.OUT)
        self._pin1 = GPIO.PWM(self._motorPort[0], 50) # frequency 50HZ by default for both pins
        self._pin2 = GPIO.PWM(self._motorPort[1], 50)
        self._pin1.ChangeDutyCycle(self._speed)
        self._pin2.ChangeDutyCycle(self._speed)
    
    def forward(self):
        self._pin2.stop()
        self._pin1.start(self._speed)
        
    def backward(self):
        self._pin1.stop()
        self._pin2.start(self._speed)
        
    def stop(self):
        self._pin1.stop()
        self._pin2.stop()
        
    def setSpeed(self, speed):
        self._speed = speed
        self._pin1.ChangeDutyCycle(self._speed)
        self._pin2.ChangeDutyCycle(self._speed)
        
    def getSpeed(self):
        return self._speed