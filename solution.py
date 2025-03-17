import numpy as np
import pyrosim.pyrosim as pyrosim
import os
import random
class SOLUTION:
    def __init__(self):
        self.weights = 2* np.random.rand(3, 2) - 1

    def Evaluate(self, directOrGUI):
        self.Create_World()
        self.Create_Body()
        self.Create_Brain()
        os.system(f"python simulate.py {directOrGUI}")
        f=open('fitness.txt','r')
        contents=f.read()
        f.close()
        self.fitness=float(contents)
        # print('self.fitness: ',self.fitness)

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


    def Create_Brain(self):
        pyrosim.Start_NeuralNetwork("brain.nndf")
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