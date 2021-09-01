import random
import numpy as np

from functions import initialize


M = 10

if __name__ == "__main__":
    monkeys = initialize.initialize_positions(3)
    print(initialize.random_vector())
    print(initialize.objective(monkeys[0]))


