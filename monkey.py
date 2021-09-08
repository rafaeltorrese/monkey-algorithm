# %%
import random
import numpy as np

from functions import initialize


M = 10
# %%
if __name__ == "__main__":
    monkeys = initialize.initialize_positions(3)
    v = initialize.generate_deltas(monkeys, a=0.0001)
    pseudograd_matrix = initialize.pseudogradient_function(monkeys, v)
    print(pseudograd_matrix)


# %%
