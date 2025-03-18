import os
# from hillclimber import HILLCLIMBER

# hc = HILLCLIMBER()

# hc.Evolve()
# hc.Show_Best()
from parallelHillClimber import PARALLEL_HILLCLIMBER

phc = PARALLEL_HILLCLIMBER()

phc.Evolve()
phc.Show_Best()