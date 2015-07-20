#!/usr/bin/python

from LegoPi import *

touchSensor = TouchSensor(3)

print "Starting daemon..."

while True:
    print "Checking for touchsensor..."
    delay(500)
    if touchSensor.isPressed():
        print "Touchsensor clicked..."
        execfile("Run.py")
        delay(2000)
        
print "Script finished"