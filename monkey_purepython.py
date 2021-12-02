import statistics
import math
import random


def f(x):
    '''Objective Function'''
    expr1 = math.sin(2 * math.pi * x[0]) ** 3
    expr2 = math.sin(2 * math.pi * x[1])
    expr3 = x[0] ** 3 * (x[0] + x[1])
    return (expr1 * expr2) / expr3


def constraint1(x: list):
    '''Constraint'''
    return x[0] ** 2 - x[1] + 1 <= 0


def constraint2(x):
    return 1 - x[0] + (x[1] - 4) ** 2 <= 0


def feasible_position(x, *constraints):
    return all([constraint(x) for constraint in constraints])


def position(n=2):
    x = [random.uniform(0, 10) for _ in range(n)]
    while not feasible_position(x, constraint1, constraint2):
        x = [random.uniform(0, 10) for _ in range(n)]
    return x


def population():
    return [position() for _ in range(M)]


def climb():
    for _ in range(Nc):
        for i, monkey in enumerate(monkeys):
            probabilities = [random.random() for _ in range(len(monkey))]
            deltas = [a if p < 0.5 else -a for p in probabilities]
            argument1 = [x + delta for x, delta in zip(monkey, deltas)]
            argument2 = [x - delta for x, delta in zip(monkey, deltas)]
            deltas_double = [2 * delta for delta in deltas]
            numerator = f(argument1) - f(argument2)
            pseudogradient = [numerator / d2 for d2 in deltas_double]
            y = [x + a * (fj / abs(fj))
                 for x, fj in zip(monkey, pseudogradient)]
            if feasible_position(y, constraint1, constraint2):
                monkeys[i] = y


def watch():
    for i, monkey in enumerate(monkeys):
        y = [random.uniform(x - b, x + b) for x in monkey]
        while not feasible_position(y, constraint1, constraint2):
            y = [random.uniform(x - b, x + b) for x in monkey]
        if f(y) >= f(monkey):
            monkeys[i] = y


def somersault():
    for i, monkey in enumerate(monkeys):
        alfa = random.uniform(c, d)
        somersault_pivot = [statistics.mean(
            monkeys[row][col] for row in range(M)) for col in range(len(monkey))]
        y = [x + alfa * (pj - x) for x, pj in zip(monkey, somersault_pivot)]
        while not feasible_position(y, constraint1, constraint2):
            alfa = random.uniform(c, d)
            y = [x + alfa * (pj - x)
                 for x, pj in zip(monkey, somersault_pivot)]
        monkeys[i] = y


def monkey_algorithm():
    z = max(f(x) for x in monkeys)
    for _ in range(N):
        climb()
        watch()
        climb()
        somersault()
        znew = max(f(x) for x in monkeys)
        if znew > z:
            z = znew
    print(f'Best Objective Value {z}')
    return z


if __name__ == '__main__':
    M = 5
    N = 10
    Nc = 2000
    a, b = 1e-5, 0.5
    c, d = -1, 1

    runs = 20
    fvalues = []

    for run in range(runs):
        print(f'Run {run + 1}')
        monkeys = population()
        fvalues.append(monkey_algorithm())

    expected = statistics.mean(fvalues)
    variance = statistics.variance(fvalues)

    print(f'Mean: {expected}')
    print(f'Variance: {variance}')
