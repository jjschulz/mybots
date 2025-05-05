import numpy as np
import matplotlib.pyplot as plt

a_matrices = [np.load(f'data/fitness_A_matrix{i}.npy') for i in range(10)]
avg_fitness_A_matrix = np.mean(a_matrices, axis=0)
avg_fitness_A = np.mean(avg_fitness_A_matrix, axis=0)

#load and average a and b matrices
b_matrices = [np.load(f'data/fitness_B_matrix{i}.npy') for i in range(10)]
avg_fitness_B_matrix = np.mean(b_matrices, axis=0)
avg_fitness_B = np.mean(avg_fitness_B_matrix, axis=0)

#plot
plt.plot(avg_fitness_A, label='A AVG')
plt.plot(avg_fitness_B, label='B AVG')

plt.xlabel('Generation')
plt.ylabel('Average Fitness')
plt.title('Average Fitness as generation evolves (A vs. B)')
plt.legend()
plt.grid(True)
plt.show()