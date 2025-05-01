import pybullet as p
import pyrosim.pyrosim as pyrosim
from sensor import SENSOR
from motor import MOTOR
from pyrosim.neuralNetwork import NEURAL_NETWORK
import os
import constants as c

class ROBOT:
    def __init__(self, solutionID):
        self.robotId=p.loadURDF('body.urdf')
        self.nn = NEURAL_NETWORK(f"brain{solutionID}.nndf")
        os.system(f"del brain{solutionID}.nndf")
    
    def Prepare_To_Sense(self):
        self.sensors = {}
        for linkName in pyrosim.linkNamesToIndices:
            self.sensors[linkName] = SENSOR(linkName)

    def Sense(self, i):
        for linkName in self.sensors:
            self.sensors[linkName].Get_Value(i)
        
    def Prepare_To_Act(self):
        self.motors = {}
        for jointName in pyrosim.jointNamesToIndices:
            self.motors[jointName] = MOTOR(jointName)

    def Act(self,desiredAngle):
        for neuronName in self.nn.Get_Neuron_Names():
            if self.nn.Is_Motor_Neuron(neuronName):
                jointName = self.nn.Get_Motor_Neurons_Joint(neuronName).encode('utf-8')
                desiredAngle = self.nn.Get_Value_Of(neuronName)*c.motorJointRange
                self.motors[jointName].Set_Value(desiredAngle, self.robotId)
                # print(neuronName)
                # print("joint name: ", jointName)
                # print('desired angle: ', desiredAngle)
       
    def Think(self):
        self.nn.Update()
        #self.nn.Print()

    def Get_Fitness(self,solutionID, avg_height, height_fitness):
        # stateOfLinkZero=p.getLinkState(self.robotId,0)
        # positionOfLinkZero = stateOfLinkZero[0]
        # xCoordinateOfLinkZero= positionOfLinkZero[0]
        basePositionAndOrientation = p.getBasePositionAndOrientation(self.robotId)
        basePosition = basePositionAndOrientation[0]
        xCoordinateOfLinkZero = basePosition[0]
        fitness=abs(xCoordinateOfLinkZero* 1/2) * avg_height
        height_fit = abs(xCoordinateOfLinkZero* 1/2) * height_fitness
        print(f'\nhere is my avg height: {avg_height}\nhere is my x value: {xCoordinateOfLinkZero}\nhere is my overall fitness:{fitness}')
        with open(f'tmp{solutionID}.txt', 'w') as f:
            f.write(str(fitness))

        with open(f'temp{solutionID}.txt', 'w') as f:
            f.write(str(height_fit))

        os.rename("tmp"+str(solutionID)+".txt" , "fitness"+str(solutionID)+".txt")
        os.rename("temp"+str(solutionID)+".txt" , "height_A_fitness"+str(solutionID)+".txt")
        