#!/usr/bin/python

import time
import RPi.GPIO as GPIO
from enum import Enum
import spidev
import time
import os

# ports for motors and sensors
class Port(Enum):
    A = [16, 15]
    B = [23, 26]
    C = 3
    D = 4


# global functions 

def delay(ms):
    time.sleep(ms*0.001)

    
# sensors
class Sensor:
    
    _port = None
    
    def __init__(self, port):
        assert isinstance(port, Port)
        self._setupPins(port)
        self._port = port;

class LightSensor(Sensor):
    
    _spi = None
    
    def __init__(self, port):
        super().__init__(port)
        self._openSPIBus()
    
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
    
    def getValue(self, lightChannel):
        lightLevel = 1024 - _readChannel(lightChannel)
        lightVolts = _convertVolts(lightLevel,2)
        return lightVolts

class TouchSensor(Sensor):
    
    def __init__(self, port):
        super().__init__(port)
        self._setupPin()
    
    def _setupPin(self):
        GPIO.setmode(GPIO.BCM) 
        GPIO.setup(_self.port.value[0], GPIO.IN, pull_up_down = GPIO.PUD_UP)
    
    def isPressed():
        if GPIO.input(_self.port.value[0]):
            return false
        else:
            return true
    
# motor
class Motor:
    
    _port = None
    _speed = 50
    
    def __init__(self, port):
        assert isinstance(port, Port)
        self._port = port;
        self._setupPins()
    
    def _setupPins(self):
        GPIO.setmode(GPIO.BCM)       
        GPIO.setup(self._port.value[0], GPIO.OUT)    
        GPIO.setup(self._port.value[1], GPIO.OUT)
        pin1 = GPIO.PWM(self._port.value[0], self._speed) // frequency 50HZ by default for both pins
        pin2 = GPIO.PWM(self._port.value[1], self._speed)
        pin1.ChangeDutyCycle(self._speed)
        pin2.ChangeDutyCycle(self._speed)
    
    def forward(self):
        GPIO.output(self._port.value[1], GPIO.LOW)
        time.sleep(0.01)
        GPIO.output(self._port.value[0], GPIO.HIGH)
        time.sleep(0.01)
        
    def backwards(self):
        GPIO.output(self._port.value[0], GPIO.LOW)
        time.sleep(0.01)
        GPIO.output(self._port.value[1], GPIO.HIGH)
        time.sleep(0.01)
        
    def stop(self):
        GPIO.output(self._port.value[0], GPIO.LOW)
        time.sleep(0.01)
        GPIO.output(self._port.value[1], GPIO.LOW)
        time.sleep(0.01)
        
    def setSpeed(self, speed):
        self._speed = speed
        
    def getSpeed(self):
        return self._speed