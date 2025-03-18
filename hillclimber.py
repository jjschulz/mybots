from solution import SOLUTION
import constants as c
import copy

class HILLCLIMBER:
    def __init__(self):
        self.parent = SOLUTION()

    def Evolve(self):
        self.parent.Evaluate('GUI')
        for currentGeneration in range(c.numberOfGenerations):
            self.Evolve_For_One_Generation()

    def Evolve_For_One_Generation(self):
        self.Spawn()

        self.Mutate()

        self.child.Evaluate('DIRECT')
        print('\nself.child and self.parent fitness: ', self.child.fitness, self.parent.fitness)

        self.Select()

    def Show_Best(self):
        print('ok final self.parent fitness: ', self.parent.fitness)
        self.parent.Evaluate('GUI')


    def Spawn(self):
        self.child=copy.deepcopy(self.parent)

    def Mutate(self):
        self.child.Mutate()
        # print('parent weights: ',self.parent.weights)
        # print('child wieghts: ', self.child.weights)
        

    def Select(self):
        #print('parent anc child fitness: ',self.parent.fitness, self.child.fitness)
        if self.parent.fitness > self.child.fitness:
            self.parent=self.child