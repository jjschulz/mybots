import pybullet as p
import time
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy as np

physicsClient=p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0,0,-9.8)
planeId=p.loadURDF('plane.urdf')
robotId=p.loadURDF('body.urdf')

p.loadSDF('world.sdf')
pyrosim.Prepare_To_Simulate(robotId)
backLegSensorValues = np.zeros(1000)
frontLegSensorValues=np.zeros(1000)
for i in range(1000):
    p.stepSimulation()
    backLegSensorValues[i]=pyrosim.Get_Touch_Sensor_Value_For_Link("Backleg")
    frontLegSensorValues[i]=pyrosim.Get_Touch_Sensor_Value_For_Link("Frontleg")

    print(backLegSensorValues[i])
    time.sleep(.01)
    # print(i)
# print(backLegSensorValues)
np.save("data/backlegSensorVals", backLegSensorValues)
np.save("data/frontlegSensorVals", frontLegSensorValues)


p.disconnect()