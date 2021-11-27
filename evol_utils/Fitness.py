import random
import numpy as np


# FITNESS CALCULATION
def fitness_calculation(chromosome_pair: list[[...],int]) -> float:

    chromosome = chromosome_pair[0]
    t1,t2 = 0,0 #Number of queens checked in left and right diagonals
    size = len(chromosome)
    f1 = []
    f2 = []
    """
    This check if two queens atack each other in the diagonal
    """
    for i in range(0,size):
        f1.append(chromosome[i] - i)
        f2.append((1+size) - chromosome[i] - i)

    f1 = sorted(f1)
    f2 = sorted(f2)

    for i in range(1,size):
        if (f1[i] == f1[i-1]):
            t1 += 1
        if (f2[i] == f2[i-1]):
            t2 += 1

    fitness_value = t1+t2

    return fitness_value
