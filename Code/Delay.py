import time
import spidev
import time
import os

def delay(ms):
    time.sleep(ms*0.001)
    

class LightSensor(Sensor):
    
    def getValue():
        return 0.01