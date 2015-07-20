from LegoPi import *

lightSensorA = LightSensor(0)
lightSensorB = LightSensor(1)
touchSensorA = TouchSensor(2)
motorA = Motor(MotorPort.A)
motorB = Motor(MotorPort.B)
motorA.backward()
motorB.backward()

motorA.setSpeed(30)
motorB.setSpeed(30)

while not touchSensorA.isPressed():
    delay(50)
    if lightSensorA.getValue() <= 150:
        motorA.stop()
    else:
        motorA.backward()
    if lightSensorB.getValue() <= 150:
        motorB.stop()
    else: 
        motorB.backward()

motorA.forward()
motorB.forward()

delay(1000)

motorA.stop()
motorB.stop()