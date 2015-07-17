from LegoPi import *

#lightSensor = LightSensor(0)
#i = 0;
#while i < 10:
#    print(lightSensor.getValue())
#    i += 1
#    delay(500)

motorA = Motor(MotorPort.A)
motorA.forward()
motorB = Motor(MotorPort.B)
motorB.forward()

delay(1000)
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
