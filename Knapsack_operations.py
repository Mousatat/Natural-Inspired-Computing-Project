import numpy as np

#Function that randomly choose genes on chromosome based on beta's value
def Knapsack_observe(Q):

    betas = [Q[i][1] for i in range(len(Q))]
    new_chrom = np.random.rand(1,len(Q)) < np.power(betas,2)
    return new_chrom[0]

#Repair function need for removing extra weight from the backpack if it is overfilled, or put item if it is not full
def Knapsack_repair(x,v,w,C):

    while np.sum(np.multiply(w,x)) > C:
        #Delete value with greatest (w*x[i])/v score
        temp = np.multiply(np.divide(w,v),x)
        mx_pos = np.argmax(temp)
        x[mx_pos] = 0
    while np.sum(np.multiply(w,x)) <= C:
        #Add value with greatest (w*(not x[i]))/v score
        temp = np.multiply(np.divide(w,v), [(x[i] + 1) % 2 for i in range(len(x))])
        mx_pos = np.argmax(temp)
        x[mx_pos] = 1
    x[mx_pos] = 0
    return x

#Counting how much values we have in total
def Knapsack_fitness(p,v):
    pv = np.multiply(v,p)
    return np.sum(pv)