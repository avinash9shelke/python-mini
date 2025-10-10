from itertools import groupby

# Sample data
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Sort the list so group by can group correctly
numbers.sort(key=lambda x: x % 2)

# Group by even (0) or odd (1)
for key, group in groupby(numbers, key=lambda x: x % 2):
    label = 'Even' if key == 0 else 'Odd'
    print(f'{label}: {list(group)}')

