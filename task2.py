from pprint import pprint
from statistics import mean
from typing import List, Callable

import pandas as pd

N: int = 10000  # Max number


def funk(n: int) -> int:  # determined function
    if n % 2 == 0:
        return n // 2
    else:
        return 3 * n + 1


energies: List[int] = []
for a in range(1, N + 1):
    energy: int = 0
    res: int = a
    while res != 1:
        energy += 1
        res = funk(res)
    energies.append(energy)

get_indexes_by_value: Callable = lambda l, v: [index + 1 for index, value in enumerate(l) if value == v]

min_energy: int = min(energies)
print(f"Minimal energy is {min_energy} for number(s): {get_indexes_by_value(energies, min_energy)}")

max_energy: int = max(energies)
print(f"Maximal energy is {max_energy} for number(s): {get_indexes_by_value(energies, max_energy)}")

mean_energy: float = mean(energies)
print(f"Mean energy is {mean_energy}")

#
# CORRELATION

x = pd.Series(range(1, N + 1))
y = pd.Series(energies)

spearmans_corr: float = x.corr(y, method='spearman')  # Spearman's rho
print(f"Spearman's correlation coefficient between numbers and their energies is {spearmans_corr}")

# List of all energies
print(f"\nList of energies of numbers from 1 to {N} is:")
pprint(dict((i, energies[i - 1]) for i in range(1, N + 1)))
