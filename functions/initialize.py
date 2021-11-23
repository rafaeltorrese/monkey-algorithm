import math
import random
import numpy as np
from numpy.lib.utils import _getmembers


random.seed(3)


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
        2 + math.pi * x[0]) ** 3 * math.sin(2 * math.pi * x[0])
    denominator = x[0] ** 3 * (x[0] + x[1])
    return numerator / denominator


def constraint1(x):
    x1, x2 = x
    return x1 ** 2 - x2 + 1 <= 0


def constraint2(x):
    x1, x2 = x
    return 1 - x1  + (x2 - 4) ** 2 <= 0


def feasible_solution(num_var=2):
    ''' Get feasible solution 
    Parameters
    ----------
    num_var: int
        Number of independent variables
    
    Returns
    --------
    x: numpy ndarray
        Independent variables that meet all constraints
    '''
    x = generate_solution(num_var)
    feasible = test_constraints(x, constraint1, constraint2)     
    while not feasible:
        x = generate_solution(num_var)
        feasible = test_constraints(x, constraint1, constraint2)     
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
    return  np.array([feasible_solution() for _ in range(M)])


def generate_solution(n=2, randmax=10):
    return [randmax * random.random() for _ in range(n)]


def generate_deltas(population, a=0.00001, p=0.5):
    randoms = np.random.random(population.shape)
    return np.where(randoms < p, a, -a)


def pseudogradient_function(x, d):
    '''Function tha implements pseudogradient function
    x: numpy ndarray
        Monkeys Population
    d: numpy ndarray
        Delta Matrix
    '''
    f1 = x + d
    f2 = x - d
    delta_double = 2 * d
    objective = np.array(
        [objective_function(xplusdelta) - objective_function(xminusdelta) for xplusdelta, xminusdelta in zip(f1, f2)])
    return objective[:, None] / delta_double


def ymatrix(x, a, f):
    '''Function that computes y matrix
    Parameters
    ----------
    x: numpy ndarray
        Population matrix
    a: float
        step_length
    f: numpy ndarray
        Pseudogradient matrix
    
    Returns
    -------
    y: numpy ndarray
        Matrix
    '''
    return x + a * np.sign(f)


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


def climbing(M, a):
    monkeys = positions(M)    
    deltas = generate_deltas(monkeys, a)
    pseudogradients = pseudogradient_function(x=monkeys, d=deltas)     
    ys = ymatrix(x=monkeys, a=a, f=pseudogradients)    
    tests = [test_constraints(ys[i], constraint1, constraint2) for i in range(M)]
    monkeys[tests] = ys[tests]
    return np.array([objective_function(x) for x in monkeys])



if __name__ == '__main__':
    M = 3
    step_length = 0.00001
    values = climbing(M, step_length)
    print(values)
    



