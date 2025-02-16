import pybullet as p
import time
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy as np
import random

Backleg_amplitude = np.pi/7
Backleg_frequency = 6
Backleg_phaseOffset = 0

Frontleg_amplitude = np.pi/4
Frontleg_frequency = 6
Frontleg_phaseOffset = np.pi/3

physicsClient=p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0,0,-9.8)
planeId=p.loadURDF('plane.urdf')
robotId=p.loadURDF('body.urdf')

p.loadSDF('world.sdf')
pyrosim.Prepare_To_Simulate(robotId)
backLegSensorValues = np.zeros(1000)
frontLegSensorValues=np.zeros(1000)

targetAngles=np.linspace(-np.pi,np.pi,1000)
Backleg_out_array=Backleg_amplitude * np.sin(Backleg_frequency * targetAngles + Backleg_phaseOffset)

Frontleg_out_array=Frontleg_amplitude * np.sin(Frontleg_frequency * targetAngles + Frontleg_phaseOffset)

# np.save('data/BacklegSineValues', Backleg_out_array)
# np.save('data/FrontlegSineValues', Frontleg_out_array)


for i in range(1000):
    p.stepSimulation()
    backLegSensorValues[i]=pyrosim.Get_Touch_Sensor_Value_For_Link("Backleg")
    frontLegSensorValues[i]=pyrosim.Get_Touch_Sensor_Value_For_Link("Frontleg")
    
    pyrosim.Set_Motor_For_Joint(
    bodyIndex = robotId,
    jointName = b'Torso_Backleg',
    controlMode = p.POSITION_CONTROL,
    targetPosition = Backleg_out_array[i],
    maxForce = 500)
    
    pyrosim.Set_Motor_For_Joint(
    bodyIndex = robotId,
    jointName = b'Torso_Frontleg',
    controlMode = p.POSITION_CONTROL,
    targetPosition = Frontleg_out_array[i],
    maxForce = 50)


    #print(backLegSensorValues[i])
    time.sleep(.01)
    print(i)
# print(backLegSensorValues)
np.save("data/backlegSensorVals", backLegSensorValues)
np.save("data/frontlegSensorVals", frontLegSensorValues)


p.disconnect()