#itertools: product, permutations, combinations, accumulate, group by and infinite iterators

from itertools import product

colors = ['red', 'green','yellow']
sizes = ['S', 'M', 'L']

# Cartesian product of colors and sizes
combinations = product(colors, sizes)

for combo in combinations:
    print(combo)
