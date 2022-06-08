"""
NQueens problem solve by Evolutionary algorithm.

Initialise population at ramdon
1. calculate the fitness
2. sort the chromosomes

Selection
1. decide the operators
2. make seleciton

Crossover
1. calculate fitness in crossover

Mutation
1. stablish mutation probability

Evaluation
"""
import time

start_time = time.time()
import numpy as np
import random
from math import ceil
from evol_utils.Initializations import intialize_population_random
from evol_utils.Fitness import fitness_calculation
from evol_utils.Crossover import crossover, parent_comparison


def Sort(sub_li):
    sub_li.sort(key=lambda x: x[1])
    return sub_li


# RANDOM INITIALIZATION OF CHROMOSOMES
"""
Here, we initialize the population as a list of [[chromosome_1,9],[...]]
each [[...]] is a chromosome_pair
"""
population_size = 1000
board_size = 20
population = intialize_population_random(population_size, board_size)

# this line check the condition, fitness = 0
element_in_sublists = [0 in chromosome_pair[0] for chromosome_pair in population]

iterations = 0
while not (any(element_in_sublists)) and (iterations < 200):
    print(f"Iteration: {iterations}")
    iterations += 1
    # FITNESS CALCULATION
    """
    We are calculating the fitness_value of each chromosome_pair
    the function fitness_calculation gets the chromosome_pair and return an integer

    """
    for i, chromosome_pair in enumerate(population):
        fitness_value = fitness_calculation(chromosome_pair)
        population[i][1] = fitness_value

    # PARENT SELECTION
    """
    We're performnig parente selection, with two methods:
    - elite selecition
    - random selection -> crossover -> tournament selection parent vs child

    """
    ##ELITE SELCTION
    population = Sort(population)

    elite = ceil(population_size * 0.1)
    elite_chromosomes = population[0:elite]

    ##RANDOM SELECTION && CROSSOVER
    for i, chromosome_pair in enumerate(population):
        if random.random() >= 0.15:
            # creating the child with type child = [[chromosome],9]
            child = crossover(
                chromosome_pair[0],
                population[random.randint(0, population_size - 1)][0],
                board_size,
            )
            # calculating fitness value and adding it to child
            child[1] = fitness_calculation(child)
            # tournament selection
            """
            selected = parent_comparison(chromosome_pair,child)
            population[i] = selected
            """
            # Bad repo selection
            population.append(child)

    sorting = Sort(population)
    population = population[0:population_size]

    population = population[0 : population_size - elite]
    population = elite_chromosomes + population
    # CHECK FOR CONDITION
    element_in_sublists = [0 in chromosome_pair for chromosome_pair in population]
    print("iteration completed")

x = Sort(population)
for chromosome_pair in population:
    if 0 in chromosome_pair:
        print(chromosome_pair)
print(x[0])
print("Sort_1 --- %s seconds ---" % (time.time() - start_time))
