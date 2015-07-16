#!/usr/bin/python

import time
import RPi.GPIO as GPIO
from enum import Enum
import spidev
import time
import os

# ports for motors and sensors
class MotorPort(Enum):
    A = [16, 15]
    B = [23, 26]


# global functions 

def delay(ms):
    time.sleep(ms*0.001)

    
# sensors
class Sensor:
    
    _channel = None
    
    def __init__(self, channel):
        self._validateChannel(channel)        
        self._channel = channel;
        self._openSPIBus()
        
    def _validateChannel(self, channel):
        if(channel > 7 || channel < = 0)
            raise ValueError("channel must be a value between 0 and 7")
            
    def _openSPIBus(self):
        self._spi = spidev.SpiDev()
        spi.open(0,0)
    
    def _readChannel(self, channel):
        adc = self._spi.xfer2([1,(8+channel)<<4,0])
        data = ((adc[1]&3) << 8) + adc[2]
        return data
    
    def _convertVolts(data,places):
        volts = (data * 3.3) / float(1023)
        volts = round(volts,places)
        return volts
    
    def getValue(self):
        level = 1024 - _readChannel(_channel)
        volts = _convertVolts(level,2)
        return volts


class LightSensor(Sensor):
    
    _spi = None
    
    def getValue(self):
        return super(LightSensor, self).getValue()
    
class TouchSensor(Sensor):
    
    def isPressed(self):
        return (super(LightSensor, self).getValue() == 1)
    
# motor
class Motor:
    
    _motorPort = None
    _speed = 50
    
    def __init__(self, motorPort):
        assert isinstance(motorPort, MotorPort)
        self._motorPort = motorPort;
        self._setupPins()
    
    def _setupPins(self):
        GPIO.setmode(GPIO.BCM)       
        GPIO.setup(self._motorPort.value[0], GPIO.OUT)    
        GPIO.setup(self._motorPort.value[1], GPIO.OUT)
        pin1 = GPIO.PWM(self._motorPort.value[0], self._speed) // frequency 50HZ by default for both pins
        pin2 = GPIO.PWM(self._motorPort.value[1], self._speed)
        pin1.ChangeDutyCycle(self._speed)
        pin2.ChangeDutyCycle(self._speed)
    
    def forward(self):
        GPIO.output(self._motorPort.value[1], GPIO.LOW)
        time.sleep(0.01)
        GPIO.output(self._motorPort.value[0], GPIO.HIGH)
        time.sleep(0.01)
        
    def backwards(self):
        GPIO.output(self._motorPort.value[0], GPIO.LOW)
        time.sleep(0.01)
        GPIO.output(self._motorPort.value[1], GPIO.HIGH)
        time.sleep(0.01)
        
    def stop(self):
        GPIO.output(self._motorPort.value[0], GPIO.LOW)
        time.sleep(0.01)
        GPIO.output(self._motorPort.value[1], GPIO.LOW)
        time.sleep(0.01)
        
    def setSpeed(self, speed):
        self._speed = speed
        
    def getSpeed(self):
        return self._speed