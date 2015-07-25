 from LegoPi import *
    
# instanziiere Lichtsensoren für Channel 0 und 1
lightSensorA = LightSensor(0)
lightSensorB = LightSensor(1)
# instanziiere Tastsensor für Channel 2
touchSensor = TouchSensor(2)

# instanziiere Motoren A und B
motorA = Motor(MotorPort.A)
motorB = Motor(MotorPort.B)

# setze Geschwindigkeit beider Motoren auf 30
motorA.setSpeed(30)
motorB.setSpeed(30)

# fahre mit beiden Motoren vorwärts
motorA.forward()
motorB.forward()
    
# solange der Tastsensor nicht gedrück ist
while not touchSensor.isPressed():
	# warte 50 ms
 	delay(50)
	# Ist der Wert von LichtsensorA geringer 150
	if lightSensorA.getValue() <= 150:
		# stoppe MotorA
		motorA.stop()
	# Ist der Wert größer 80, fahre vorwärts
	else:
		motorA.forward()

	# Ist der Wert von LichtsensorB geringer 80
	if lightSensorB.getValue() <= 150:
		motorB.stop()
	else:
		# Ist der Wert größer 80, fahre vorwärts 
		motorB.forward()
    
# Stoppe Motor A und B
motorA.stop()
motorB.stop()