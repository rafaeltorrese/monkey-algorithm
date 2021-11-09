import math
import random
import numpy as np


random.seed(3)
RAND_MAX = 10

def objective(x):
    numerator = math.sin(2 + math.pi * x[0]) ** 3 * math.sin(2 * math.pi * x[0])
    denominator = x[0] ** 3 * (x[0] + x[1])
    return numerator / denominator 



def constraint1(x1, x2):
    return x1 ** 2 - x2 + 1 <= 0

def constraint2(x1, x2):
    return 1 - x1  + (x2 - 4) ** 2 <= 0


def feasible_solution(num_var=2):
    feasible = False
    while not feasible:
        x = generate_solution(num_var)
        constraints = [constraint1(*x), constraint2(*x)]
        feasible = all(constraints)        
    return x
        


def positions(M):
    '''This function initialize population
    
    Parameters
    ----------
    M: int
        Number of monkeys in the population
    num_vars: int
        Dimension of the problem. Number of variables.
    '''
    population = []
    for _ in range(M):
        solution = feasible_solution()
        population.append(solution)
    return np.array(population)


def generate_solution(n=2, randmax=10):
    return  [randmax * random.random() for _ in range(n)]
    
def deltas(population, a, p=0.5):
    randoms = np.random.random(population.shape)
    return np.where(randoms < p, a, -a)


def pseudogradient_function(x, deltax):
    pass

if __name__ == '__main__':
    monkeys = initialize_positions(3)
    
    



