from LegoPi import *

lightSensorA = TouchSensor(0)
lightSensorB = TouchSensor(1)
touchSensor = TouchSensor(2)
motorA = Motor(MotorPort.A)
motorA.forward()
motorB = Motor(MotorPort.B)
motorB.forward()

while not touchSensor.isPressed():
    delay(50)
    if lightSensorA.getValue() <= 80:
        motorA.stop()
    else:
        motorA.forward()
    if lightSensorB.getValue() <= 80:
        motorB.stop()
    else: 
        motorB.forward()

motorA.stop()
motorB.stop()



#lightSensor = new LightSensor(0)
#touchSensor = new TouchSensor(1)
#motorA = new Motor(MotorPort.A)
#motorB = new Motor(MotorPort.B)

#while !touchSensor.isPressed():
#    print(lightSensor.getValue())
#    delay(1000)

#print("TouchSensor is pressed")

#motorA.forward()
#delay(1000)

#motorA.backward()
#delay(1000)

#motorB.forward()
#delay(1000)

#motorB.backward()
#delay(1000)

#motorA.forward()
#motorB.forward()
#delay(1000)

#motorA.backward()
#motorB.backward()
#delay(1000)
