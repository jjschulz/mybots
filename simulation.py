import pybullet as p
import time
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy as np
from robot import ROBOT
from world import WORLD
import constants as c

class SIMULATION:
    def __init__(self, directOrGUI, solutionID):
        if directOrGUI == 'DIRECT':
            self.physicsClient=p.connect(p.DIRECT)
        else:
            self.physicsClient=p.connect(p.GUI)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        self.world = WORLD()
        p.setGravity(0,0,-9.8)
        self.robot = ROBOT(solutionID)
        pyrosim.Prepare_To_Simulate(self.robot.robotId)
        self.robot.Prepare_To_Sense()
        self.robot.Prepare_To_Act()
        self.heights=[]


    def run(self):
        for i in range(c.loopConstant):
            p.stepSimulation()
            position, orientation = p.getBasePositionAndOrientation(self.robot.robotId)
            z_value=position[2]
            self.heights.append(z_value)
            self.robot.Sense(i)
            self.robot.Think()
            self.robot.Act(i)
            time.sleep(.005)
            # print(i)
        self.avg_height=np.mean(self.heights)
        self.height_fitness=(max(self.heights)*np.mean(self.heights) )*1/2

    def Get_Fitness(self, solutionID):
        #print('here is my max height ', self.max_height)
        self.robot.Get_Fitness(solutionID, self.avg_height, self.height_fitness)


    def __del__(self):
        p.disconnect()