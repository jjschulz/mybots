from simulation import SIMULATION
import sys

directOrGUI=sys.argv[1]
simulation = SIMULATION(directOrGUI)
simulation.run()
simulation.Get_Fitness()
