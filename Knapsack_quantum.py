import numpy as np
from Knapsack_operations import Knapsack_observe, Knapsack_repair, Knapsack_fitness


def Knapsack_quantum(population_size, values, weights, capacity, iteration_number):

    ind_size = np.size(values)
    best_fitness = -1
    best_population_fitness = [0 for i in range(population_size)]
    fitness = [0 for i in range(population_size)]

    #Values for future graph plotting
    x = [i+1 for i in range(iteration_number)]
    y = []

    #Initialazing our Q-bit string, population and best_population lists
    Q = [[[1/(2**0.5), 1/(2**0.5)] for i in range(ind_size)] for i in range(population_size)]   
    p = [[0 for i in range(ind_size)] for i in range(population_size)]            
    B = [[0 for i in range(ind_size)] for i in range(population_size)]                                                              

    for i in range(iteration_number):
        for j in range(population_size):
            p[j] = Knapsack_observe(Q[j])                                              
            p[j] = Knapsack_repair(p[j], values, weights, capacity)           
            fitness[j] = Knapsack_fitness(p[j], values)    

            #Change Q-bits based on update procedure
            for k in range(len(Q[j])):
                if fitness[j] < best_population_fitness[j] and p[0][j] != B[0][j] and p[0][j] == 0:
                    teta = 0.01*np.pi
                elif fitness[j] < best_population_fitness[j] and p[0][j] != B[0][j] and p[0][j] == 1:
                    teta = -0.01*np.pi
                else:
                    teta = 0
                Q[j][k][0] = Q[j][k][0]*np.cos(teta) - Q[j][k][1]*np.sin(teta) 
                Q[j][k][1] = Q[j][k][0]*np.sin(teta) + Q[j][k][1]*np.cos(teta)                               

        #Remember chromosome with better fitness score
        for j in range(population_size):
            if fitness[j] > best_population_fitness[j]:      
                B[j] = p[j]
                best_population_fitness[j] = fitness[j]
        y.append(np.max(best_population_fitness))

    #Find best fitness score and its chromosome
    best_fitness = np.max(best_population_fitness)
    best_chromosome = B[best_population_fitness.index(best_fitness)]
    best_chromosome = [int(best_chromosome[i]) for i in range(len(best_chromosome))]

    return best_fitness, best_chromosome, x, y




