
import random


#RANDOM INITIALIZATION OF CHROMOSOMES
def intialize_population_random(population_size: int, board_size:int)-> list[...]:

    population = []
    for chromosome in range(0,population_size):
        population.append([random.sample(range(1, board_size + 1), board_size),9])

    return population
