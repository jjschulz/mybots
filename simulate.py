import pybullet as p
import time
import pybullet_data

physicsClient=p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0,0,-9.8)
planeId=p.loadURDF('plane.urdf')
p.loadSDF('boxes.sdf')

for i in range(100000):
    p.stepSimulation()
    time.sleep(.01)
    print(i)

p.disconnect()