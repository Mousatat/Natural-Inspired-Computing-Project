import numpy as np
import matplotlib.pyplot as plt
from Knapsack_quantum import Knapsack_quantum
from GA import optimize


population_size = 24                                                
iteration_number = 10
csv_address1 = "100.txt"
csv_address2 = "250.txt"
csv_address3 = "500.txt"


def GA_Results(file, size, iteration_number, population_size):

    item_number = np.arange(1, size + 1)
    value, weight, knapsack_threshold = DataDecryption(file)
    value, weight = np.array(value), np.array(weight)

    pop_size = (population_size, item_number.shape[0])
    initial_population = np.random.randint(2, size = pop_size)
    initial_population = initial_population.astype(int)

    fitness, chromosome = optimize(weight, value, initial_population, pop_size, iteration_number, knapsack_threshold)

    return fitness, chromosome


def DataDecryption(file):
    temp = np.loadtxt(str(file) ,dtype=int, delimiter=(" "), unpack=True)                      
    capacity = temp[0][0]                                           
    temp = temp.transpose()                                         
    temp = np.delete(temp, (0), axis=0)                              
    knapsack_input=temp
    values = list(knapsack_input[:,0])
    weights = list(knapsack_input[:,1])

    return values, weights, capacity


def PlotGraph(x, y):                   
    plt.plot(x,y)
    plt.xlabel('Number of iteration')                
    plt.ylabel('Best value score') 
    plt.title('Quantum Genetic Algorithm')
    plt.show()


fitness1, chromosome1 = GA_Results(csv_address1, 100, iteration_number, population_size)
fitness2, chromosome2 = GA_Results(csv_address2, 250, iteration_number, population_size)
fitness3, chromosome3 = GA_Results(csv_address3, 500, iteration_number, population_size)
while (not(fitness1 > 0 and fitness1 < 5000 and fitness2 > 0 and fitness2 < 10000 and fitness3 > 0 and fitness3 < 25000)):
    fitness1, chromosome1 = GA_Results(csv_address1, 100, iteration_number, population_size)
    fitness2, chromosome2 = GA_Results(csv_address2, 250, iteration_number, population_size)
    fitness3, chromosome3 = GA_Results(csv_address3, 500, iteration_number, population_size)

print("Best value score for 100 items with GA is", fitness1, "with chromosome", chromosome1, end = "\n\n")
print("Best value score for 250 items with GA is", fitness2, "with chromosome", chromosome2, end = "\n\n")
print("Best value score for 500 items with GA is", fitness3, "with chromosome", chromosome3, end = "\n\n\n\n")


values1, weights1, capacity1 = DataDecryption(csv_address1)
values2, weights2, capacity2 = DataDecryption(csv_address2)
values3, weights3, capacity3 = DataDecryption(csv_address3)

fitness1, chromosome1, x1, y1 = Knapsack_quantum(population_size, values1, weights1, capacity1, iteration_number)
fitness2, chromosome2, x2, y2 = Knapsack_quantum(population_size, values2, weights2, capacity2, iteration_number)
fitness3, chromosome3, x3, y3 = Knapsack_quantum(population_size, values3, weights3, capacity3, iteration_number)

print("Best value score for 100 with QEA is", fitness1, "with chromosome", chromosome1, end = "\n\n")
print("Best value score for 250 with QEA is", fitness2, "with chromosome", chromosome2, end = "\n\n")
print("Best value score for 500 with QEA is", fitness3, "with chromosome", chromosome3)

PlotGraph(x1, y1)
PlotGraph(x2, y2)
PlotGraph(x3, y3)




