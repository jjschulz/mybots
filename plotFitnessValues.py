import numpy as np
import matplotlib.pyplot

fitness_B_matrix = np.load('fitness_B_matrix.npy')
fitness_A_matrix = np.load('fitness_A_matrix.npy')

matplotlib.pyplot.plot(fitness_B_matrix[0,:])
matplotlib.pyplot.plot(fitness_A_matrix[0,:])

matplotlib.pyplot.show()