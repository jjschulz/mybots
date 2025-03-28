import numpy as np
import pyrosim.pyrosim as pyrosim
import os
import random
import time
class SOLUTION:
    def __init__(self, ID):
        self.weights = 2* np.random.rand(9,8) - 1
        self.myID = ID

    def Evaluate(self, directOrGUI):
        self.Create_World()
        self.Create_Body()
        self.Create_Brain(self.myID)
        os.system(f"start /B python simulate.py {directOrGUI} {str(self.myID)} 2>&1 &")
        while not os.path.exists(f'fitness{str(self.myID)}.txt'):
            time.sleep(0.01)
        f=open(f'fitness{str(self.myID)}.txt','r')
        contents=f.read()
        f.close()
        self.fitness=float(contents)
        print(f'here is my new self.fitness: {self.fitness}')
        # print('self.fitness: ',self.fitness)

    def Start_Simulation(self, directOrGUI):
        self.Create_World()
        self.Create_Body()
        self.Create_Brain(self.myID)
        os.system(f"start /B python simulate.py {directOrGUI} {str(self.myID)}")

    def Wait_For_Simulation_To_End(self):
        while not os.path.exists(f'fitness{str(self.myID)}.txt'):
            time.sleep(0.02)
        f=open(f'fitness{str(self.myID)}.txt','r')
        contents=f.read()
        f.close()
        self.fitness=float(contents)
        # print(f'here is my new self.fitness: {self.fitness}')
        os.system(f'del fitness{self.myID}.txt')

    def Set_ID(self):
        self.myID

    def Create_World(self):
        pyrosim.Start_SDF('world.sdf')
        length=1
        width=1
        height=1
        x=-3
        y=3
        z=0.5
        pyrosim.Send_Cube(name='Box', pos=[x,y,z], size=[length, width, height])
        pyrosim.End()

    def Create_Body(self):
        pyrosim.Start_URDF("body.urdf")
        length=1
        width=1
        height=1
        x=0
        y=0
        z=1.5
        pyrosim.Send_Cube(name='Torso', pos=[0,0,1], size=[length, width, height])
        pyrosim.Send_Joint( name = "Torso_Frontleg" , parent= "Torso" , child = "Frontleg" , type = "revolute", position = [0,0.5,1], jointAxis = "1 0 0")
        pyrosim.Send_Cube(name='Frontleg', pos=[0,0.5,0], size=[0.2,1,0.2])
        pyrosim.Send_Joint( name = "Torso_Backleg" , parent= "Torso" , child = "Backleg" , type = "revolute", position = [0,-0.5,1], jointAxis= "1 0 0")
        pyrosim.Send_Cube(name='Backleg', pos=[0,-0.5,0], size=[0.2,1,0.2])
        pyrosim.Send_Joint( name = "Torso_Leftleg" , parent= "Torso" , child = "Leftleg" , type = "revolute", position = [-0.5,0,1], jointAxis= "0 1 0")
        pyrosim.Send_Cube(name='Leftleg', pos=[-0.5,0,0], size=[1,0.2,0.2])
        pyrosim.Send_Joint( name = "Torso_Rightleg" , parent= "Torso" , child = "Rightleg" , type = "revolute", position = [0.5,0,1], jointAxis= "0 1 0")
        pyrosim.Send_Cube(name='Rightleg', pos=[0.5,0,0], size=[1,0.2,0.2])

        pyrosim.Send_Joint( name = "Frontleg_FrontLowerLeg" , parent= "Frontleg" , child = "FrontLowerLeg" , type = "revolute", position = [0,1,0], jointAxis= "1 1 1")
        pyrosim.Send_Cube(name='FrontLowerLeg', pos=[0,0,-0.5], size=[0.2,0.2,1])
        pyrosim.Send_Joint( name = "Backleg_BackLowerLeg" , parent= "Backleg" , child = "BackLowerLeg" , type = "revolute", position = [0,-1,0], jointAxis= "1 1 1")
        pyrosim.Send_Cube(name='BackLowerLeg', pos=[0,0,-0.5], size=[0.2,0.2,1])

        pyrosim.Send_Joint( name = "Leftleg_LeftLowerLeg" , parent= "Leftleg" , child = "LeftLowerLeg" , type = "revolute", position = [-1,0,0], jointAxis= "1 1 1")
        pyrosim.Send_Cube(name='LeftLowerLeg', pos=[0,0,-0.5], size=[0.2,0.2,1])
        pyrosim.Send_Joint( name = "Rightleg_RightLowerLeg" , parent= "Rightleg" , child = "RightLowerLeg" , type = "revolute", position = [1,0,0], jointAxis= "1 1 1")
        pyrosim.Send_Cube(name='RightLowerLeg', pos=[0,0,-0.5], size=[0.2,0.2,1])

        pyrosim.End()


    def Create_Brain(self, id):
        pyrosim.Start_NeuralNetwork(f"brain{id}.nndf")
        pyrosim.Send_Sensor_Neuron(name = 0 , linkName = "Torso")
        pyrosim.Send_Sensor_Neuron(name = 1 , linkName = "Backleg")
        pyrosim.Send_Sensor_Neuron(name = 2 , linkName = "Frontleg")
        pyrosim.Send_Sensor_Neuron(name = 3 , linkName = "Leftleg")
        pyrosim.Send_Sensor_Neuron(name = 4 , linkName = "Rightleg")
        pyrosim.Send_Sensor_Neuron(name = 5 , linkName = "BackLowerLeg")
        pyrosim.Send_Sensor_Neuron(name = 6 , linkName = "FrontLowerLeg")
        pyrosim.Send_Sensor_Neuron(name = 7 , linkName = "LeftLowerLeg")
        pyrosim.Send_Sensor_Neuron(name = 8 , linkName = "RightLowerLeg")
        pyrosim.Send_Motor_Neuron( name = 9 , jointName = "Torso_Backleg")
        pyrosim.Send_Motor_Neuron( name = 10 , jointName = "Torso_Frontleg")
        pyrosim.Send_Motor_Neuron( name = 11 , jointName = "Torso_Leftleg")
        pyrosim.Send_Motor_Neuron( name = 12 , jointName = "Torso_Rightleg")
        pyrosim.Send_Motor_Neuron( name = 13 , jointName = "Frontleg_FrontLowerLeg")
        pyrosim.Send_Motor_Neuron( name = 14 , jointName = "Backleg_BackLowerLeg")
        pyrosim.Send_Motor_Neuron( name = 15 , jointName = "Leftleg_LeftLowerLeg")
        pyrosim.Send_Motor_Neuron( name = 16 , jointName = "Rightleg_RightLowerLeg")
        for currentRow in range(9):
            for currentColumn in range(8):
                pyrosim.Send_Synapse(sourceNeuronName=currentRow, targetNeuronName=currentColumn+9,weight=self.weights[currentRow][currentColumn])
        pyrosim.End()


    def Mutate(self):
        randrow=random.randint(0,8)
        randcol=random.randint(0,7)
        self.weights[randrow][randcol]=random.random()*2 - 1