import math
import statistics
import random
from pprint import pprint
import numpy as np
from numpy.lib.utils import _getmembers
from numpy.random import rand


# random.seed(3)


def objective_function(x):
    '''Function that computes objective function
    Parameters
    ----------
    x: numpy ndarray
        Vector with decision variables
    Returns
    -------
    value: real
        Value of objective function.
    '''
    numerator = math.sin(
        2 * math.pi * x[0]) ** 3 * math.sin(2 * math.pi * x[1])
    denominator = x[0] ** 3 * (x[0] + x[1])
    return numerator / denominator


def constraint1(x):
    x1, x2 = x
    return x1 ** 2 - x2 + 1 <= 0


def constraint2(x):
    x1, x2 = x
    return 1 - x1 + (x2 - 4) ** 2 <= 0


def feasible_solution(num_var=2, randmax=10):
    ''' Get feasible solution 
    Parameters
    ----------
    num_var: int
        Number of independent variables
    randmax: int
        Max interval

    Returns
    --------
    x: numpy ndarray
        Independent variables that meet all constraints
    '''
    feasible = False
    while not feasible:
        x = [randmax * random.random() for _ in range(num_var)]
        feasible = test_constraints(x, constraint1, constraint2)
    return x


def generate_solution(randmax=10, num_var=2):
    return [randmax * random.random() for _ in range(num_var)]


def population(M):
    '''This function initialize population

    Parameters
    ----------
    M: int
        Number of monkeys in the population
    num_vars: int
        Dimension of the problem. Number of variables.
    '''
    return np.array([feasible_solution() for _ in range(M)])


def test_constraints(x, *constraints):
    '''Function tha test feasibility in all constraints in the problem
    Parameters
    -----------
    x: numpy ndarray
        n-dimensional point
    constraints: function
        Constraint of the problem
    Returns
    --------
    Bool
        Test all constraints in x
    '''
    evaluations = [constraint(x) for constraint in constraints]
    return all(evaluations)


def climbing():
    '''Climbing process
    monkeys: numpy ndarray
        Monkey Population
    Nc: int
        Number of climbings
    a: float
        Step length
    p = float
    '''
    i, j = monkeys.shape
    for c in range(Nc):
        for i, monkey in enumerate(monkeys):
            r = np.random.random(j)
            delta = np.where(r < 0.5, a, -a)
            f1 = objective_function(monkey + delta)
            f2 = objective_function(monkey - delta)
            f = np.divide(f1 - f2, 2 * delta)
            y = monkey + a * np.sign(f)
            if test_constraints(y, constraint1, constraint2):
                monkeys[i] = y


def watch():
    '''Watch Process
    monkeys: numpy ndarray
        Population of m monkeys
    '''
    for i, monkey in enumerate(monkeys):
        feasible = False
        while not feasible:
            y = np.array([random.uniform(x - b, x + b) for x in monkey])
            feasible = test_constraints(y, constraint1, constraint2)
        if objective_function(y) >= objective_function(monkey):
            monkeys[i] = y


def somersault():
    ''' Somersault Process
    monkeys: numpy ndarray
        Population
    c, d: int
        Somersault Interval
    '''
    somersault_pivot = monkeys.mean(axis=0)  # mean by columns
    for i, monkey in enumerate(monkeys):
        feasible = False
        while not feasible:
            y = [x + random.uniform(c, d) * (p - x)
                 for x, p in zip(monkey, somersault_pivot)]
            feasible = test_constraints(y, constraint1, constraint2)
        monkeys[i] = y


def monkey_algorithm():
    fvalues = []
    z = max([objective_function(x) for x in monkeys])
    for iteration in range(N):
        climbing()
        watch()
        climbing()
        somersault()
        z2 = max([objective_function(x) for x in monkeys])
        if z2 > z:
            z = z2
        # print(f'Iteration no: {iteration + 1}. Best value: {z}')
        fvalues.append(z)
    return z

    pass


if __name__ == '__main__':
    N = 10  # Whole Iterations
    M = 5   # Monkeys
    Nc = 200  # Number of climbs
    a = 1e-4  # step length
    b = 0.5  # eyesight
    c, d = -1, 1  # somersault interval
    trials = 20  # runs
    results = []
    for trial in range(trials):
        monkeys = population(M)
        results.append(monkey_algorithm())
        print(f'Trial number: { trial + 1}')
    print('Results')
    pprint(results)
    print(f'Mean: {statistics.mean(results)}')
    print(f'Variance: {statistics.variance(results)}')
    print(f'StdDev: {statistics.stdev(results)}')
