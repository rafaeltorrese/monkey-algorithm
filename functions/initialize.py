import math
import random
import numpy as np


random.seed(3)


def objective_function(x):
    numerator = math.sin(
        2 + math.pi * x[0]) ** 3 * math.sin(2 * math.pi * x[0])
    denominator = x[0] ** 3 * (x[0] + x[1])
    return numerator / denominator


def constraint1(x):
    return x[0] ** 2 - x[1] + 1

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
    return [randmax * random.random() for _ in range(n)]


def generate_deltas(population, a=0.001, p=0.5):
    randoms = np.random.random(population.shape)
    return np.where(randoms < p, a, -a)


def pseudogradient_function(monkey, deltax):
    f1 = monkey + deltax
    f2 = monkey - deltax
    delta_double = 2 * deltax
    objective = np.array(
        [objective_function(x1) - objective_function(x2) for x1, x2 in zip(f1, f2)])
    return objective[:, None] / delta_double


if __name__ == '__main__':
    monkeys = initialize_positions(3)
    
    



