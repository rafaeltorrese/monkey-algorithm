#%%
import random
import numpy as np

from functions import initialize


M = 10
#%%
if __name__ == "__main__":
    monkeys = initialize.initialize_positions(3)
    v = initialize.deltas(monkeys, a=0.0001)
    print(v)
    print(monkeys[0])
    print(v[0])
    print(monkeys[0] + v[0])
    print(monkeys[0] - v[0])
    print('objectives')
    print(initialize.objective(monkeys[0]))
    print(initialize.objective(monkeys[0] + v[0]))
    print(initialize.objective(monkeys[0] - v[0]))
    f1 = initialize.objective(monkeys[0] + v[0])
    f2 = initialize.objective(monkeys[0] - v[0])
    print(f1 - f2)
    print((f1 - f2) / 2 * v[0] )
    # print(monkeys)

# %%
