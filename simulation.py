import pybullet as p
import time
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy as np
from robot import ROBOT
from world import WORLD
import constants as c

class SIMULATION:
    def __init__(self):
        self.physicsClient=p.connect(p.GUI)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        self.world = WORLD()
        p.setGravity(0,0,-9.8)
        self.robot = ROBOT()
        pyrosim.Prepare_To_Simulate(self.robot.robotId)
        self.robot.Prepare_To_Sense()
        self.robot.Prepare_To_Act()


    def run(self):
        for i in range(c.loopConstant):
            p.stepSimulation()
            self.robot.Sense(i)
            self.robot.Think()
            self.robot.Act(i)
            time.sleep(.01)
            # print(i)


    def __del__(self):
        p.disconnect()