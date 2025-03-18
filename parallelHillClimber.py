from solution import SOLUTION
import constants as c
import copy
import os

class PARALLEL_HILLCLIMBER:
    def __init__(self):
        os.system('del brain*.nndf')
        os.system('del fitness*.txt')
        self.parents = {}
        self.nextAvailableID = 0
        for i in range(0,c.populationSize):
            self.parents[i]=SOLUTION(self.nextAvailableID)
            self.nextAvailableID+=1
        

        
    def Evaluate(self, solutions):
        for parent in solutions.values():
            parent.Start_Simulation('DIRECT')
        for parent in solutions.values():
            parent.Wait_For_Simulation_To_End()
            # print('fitness: ', parent.fitness)

    def Evolve(self):
        self.Evaluate(self.parents)
        for currentGeneration in range(c.numberOfGenerations):
            self.Evolve_For_One_Generation()
        

    def Evolve_For_One_Generation(self):
        self.Spawn()

        self.Mutate()

        self.Evaluate(self.children)
        for i in self.parents.keys():
            print(f'self.child and self.parent fitness: ', self.children[i].fitness, self.parents[i].fitness)

        self.Select()

    def Show_Best(self):
        # print('ok final self.parent: ', self.parent.fitness)
        # self.parent.Evaluate('GUI')
        lowest=100
        lowest_parent=None
        for parent in self.parents.values():
            if parent.fitness < lowest:
                lowest=parent.fitness
                lowest_parent=parent
        print('ok final parent fitness: ', lowest_parent.fitness)
        lowest_parent.Start_Simulation('GUI')

    def Spawn(self):
        self.children={}
        for key in self.parents.keys():
            self.children[key]=copy.deepcopy(self.parents[key])
            self.children[key].Set_ID()
            self.nextAvailableID+=1
        #self.child=copy.deepcopy(self.parent)

    def Mutate(self):
        for child in self.children.values():
            child.Mutate()
        # print('parent weights: ',self.parent.weights)
        # print('child wieghts: ', self.child.weights)
        

    def Select(self):
        #print('parent anc child fitness: ',self.parent.fitness, self.child.fitness)
        for key in self.parents.keys():
            if self.children[key].fitness < self.parents[key].fitness:
                self.parents[key]=self.children[key]
        # if self.parent.fitness > self.child.fitness:
        #     self.parent=self.child