from itertools import permutations

items = ['A', 'B', 'C']

# Generate all permutations of length 3 (default is full length)
permutations_list = list(permutations(items, 3))

for permutation in permutations_list:
    print(permutation)
