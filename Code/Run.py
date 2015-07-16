from LegoPi import *

lightSensor = new LightSensor(0)
touchSensor = new TouchSensor(1)
motorA = new Motor(MotorPort.A)
motorB = new Motor(MotorPort.B)

while !touchSensor.isPressed():
    print(lightSensor.getValue())
    delay(1000)

print("TouchSensor is pressed")

motorA.forward()
delay(1000)

motorA.backward()
delay(1000)

motorB.forward()
delay(1000)

motorB.backward()
delay(1000)

motorA.forward()
motorB.forward()
delay(1000)

motorA.backward()
motorB.backward()
delay(1000)
