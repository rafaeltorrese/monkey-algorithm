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
    return x1 ** 2 - x2 + 1 

def constraint2(x1, x2):
    return 1 - x1  + (x2 - 4) ** 2


def initialize_positions(M, num_var=2):
    population = []
    for _ in range(M):
        x = generate_solution(num_var)
        feasible = False
        while not feasible:
            if constraint1(*x) > 0:
                x = generate_solution(num_var)
                continue        
            if constraint2(*x) > 0:                            
                x = generate_solution(num_var)
                continue
            feasible = True
        population.append(x)
    return population


def rand_integer(r):
    return random.randint(0, r - 1)

def generate_solution(n=2, randmax=10):
    return  [randmax * random.random() for _ in range(n)]
    
def random_vector(a=0.0001, n=2):
    return [a if random.random() < 0.5 else -1.0 * a for _ in range(n)]


def pseudogradient_function(x, deltax):
    pass

if __name__ == '__main__':
    monkeys = initialize_positions(3)
    print(random_vector(0.00001, 4))
    



