import numpy as np
import matplotlib.pyplot

fitness_B_matrix = np.load('fitness_B_matrix.npy')
fitness_A_matrix = np.load('fitness_A_matrix.npy')

avg_fitness_A = np.mean(fitness_A_matrix, axis=0)
avg_fitness_B = np.mean(fitness_B_matrix, axis=0)

matplotlib.pyplot.plot(avg_fitness_A, label='A AVG')
matplotlib.pyplot.plot(avg_fitness_B, label = 'B AVG')

matplotlib.pyplot.xlabel('Generation')
matplotlib.pyplot.ylabel('Average Fitness')
matplotlib.pyplot.title('Average Fitness per Generation (A vs. B)')
matplotlib.pyplot.legend()
matplotlib.pyplot.grid(True)

matplotlib.pyplot.show()