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


def constraint2(x):
    return 1 - x[0] + (x[1] - 4) ** 2


def initialize_positions(M, num_var=2):
    population = []
    for _ in range(M):
        x = generate_solution(num_var)
        feasible = False
        while not feasible:
            if constraint1(x) > 0:
                x = generate_solution(num_var)
                continue
            if constraint2(x) > 0:
                x = generate_solution(num_var)
                continue
            feasible = True
        population.append(x)
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
    deltax = generate_deltas(monkeys, a=0.0001)
    pseudof = pseudogradient_function(monkeys, deltax)
    print(pseudof)
    print(np.sign(pseudof[0]))
