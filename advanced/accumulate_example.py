from itertools import accumulate

numbers = [1, 2, 3, 4, 5]

# Default behavior: cumulative sum
result = list(accumulate(numbers))
print(result)