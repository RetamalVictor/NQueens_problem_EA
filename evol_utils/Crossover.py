
import random


def crossover(parent_1: list[...], parent_2:list[...], board_size: int) -> list[...]:
    #selecting random points to create allele
    first_point = random.randint(0,6)
    second_point = random.randint(first_point+1,7)

    child = l = [None] * board_size
    alleles = parent_1[first_point:second_point+1]

    for i, allele in enumerate(alleles):
        child[first_point+i] = allele

    for i, allele in enumerate(child):
        if child[i] == None:
            for j in parent_2:
                if not (j in child):
                    child[i] = j
                    break

    return[child,9]

def Sort(sub_li):
	sub_li.sort(key = lambda x: x[1])
	return sub_li

def parent_comparison(parent_1: list[...], child: list[...]) -> list[...]:
    sample = [parent_1,child]
    sample = Sort(sample)

    return sample[0]



"""
Tests
parent_1 = [[6, 5, 8, 4, 7, 1, 3, 2], 4]
parent_2 = [5, 6, 8, 4, 7, 1, 3, 2]

child = crossover(parent_1[0],parent_2[0])

selected = parent_comparison(parent_1, child)
print("This is the child:", child)
print("This is parent_1:", parent_1)
print("This won the tournament selection:", selected)

"""
