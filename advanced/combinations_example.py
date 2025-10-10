from itertools import combinations

# Combinations with replacement
items = ['A', 'B', 'C']

# Generate all combinations of length 2
combinations_list = list(combinations(items, 2))

for c in combinations_list:
    print(c)
