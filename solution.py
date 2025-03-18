import numpy as np
import pyrosim.pyrosim as pyrosim
import os
import random
import time
class SOLUTION:
    def __init__(self, ID):
        self.weights = 2* np.random.rand(3, 2) - 1
        self.myID = ID

    def Evaluate(self, directOrGUI):
        self.Create_World()
        self.Create_Body()
        self.Create_Brain(self.myID)
        os.system(f"start /B python simulate.py {directOrGUI} {str(self.myID)}")
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
            time.sleep(0.01)
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
        z=0.5
        pyrosim.Send_Cube(name='Torso', pos=[x,y,1.5], size=[length, width, height])
        pyrosim.Send_Joint( name = "Torso_Frontleg" , parent= "Torso" , child = "Frontleg" , type = "revolute", position = [0.5,0,1])
        pyrosim.Send_Cube(name='Frontleg', pos=[0.5,0,-.5], size=[length, width, height])
        pyrosim.Send_Joint( name = "Torso_Backleg" , parent= "Torso" , child = "Backleg" , type = "revolute", position = [-0.5,0,1])
        pyrosim.Send_Cube(name='Backleg', pos=[-0.5,0,-0.5], size=[length, width, height])

        pyrosim.End()


    def Create_Brain(self, id):
        pyrosim.Start_NeuralNetwork(f"brain{id}.nndf")
        pyrosim.Send_Sensor_Neuron(name = 0 , linkName = "Torso")
        pyrosim.Send_Sensor_Neuron(name = 1 , linkName = "Backleg")
        pyrosim.Send_Sensor_Neuron(name = 2 , linkName = "Frontleg")
        pyrosim.Send_Motor_Neuron( name = 3 , jointName = "Torso_Backleg")
        pyrosim.Send_Motor_Neuron( name = 4 , jointName = "Torso_Frontleg")
        for currentRow in range(3):
            for currentColumn in range(2):
                pyrosim.Send_Synapse(sourceNeuronName=currentRow, targetNeuronName=currentColumn+3,weight=self.weights[currentRow][currentColumn])
        pyrosim.End()


    def Mutate(self):
        randrow=random.randint(0,2)
        randcol=random.randint(0,1)
        self.weights[randrow][randcol]=random.random()*2 - 1