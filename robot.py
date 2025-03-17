import pybullet as p
import pyrosim.pyrosim as pyrosim
from sensor import SENSOR
from motor import MOTOR
from pyrosim.neuralNetwork import NEURAL_NETWORK

class ROBOT:
    def __init__(self):
        self.robotId=p.loadURDF('body.urdf')
        self.nn = NEURAL_NETWORK("brain.nndf")
    
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
                desiredAngle = self.nn.Get_Value_Of(neuronName)
                self.motors[jointName].Set_Value(desiredAngle, self.robotId)
                # print(neuronName)
                # print("joint name: ", jointName)
                # print('desired angle: ', desiredAngle)
       
    def Think(self):
        self.nn.Update()
        #self.nn.Print()

    def Get_Fitness(self):
        stateOfLinkZero=p.getLinkState(self.robotId,0)
        #print('state:',stateOfLinkZero)
        positionOfLinkZero = stateOfLinkZero[0]
        #print('position: ',positionOfLinkZero)
        xCoordinateOfLinkZero= positionOfLinkZero[0]
        #print('xcoordinat: ',xCoordinateOfLinkZero)
        f=open('fitness.txt','w')
        f.write(str(xCoordinateOfLinkZero))
        f.close()
        