# lambda arguments: expression
from functools import reduce

# Lambda to add two numbers
add = lambda x, y: x + y
print(f"Addition of number - {add(5, 3)}")  # Output: 8

# Square each number in the list
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))
print(f"Squared result - {squared}")  # Output: [1, 4, 9, 16, 25]

# Filter even numbers
numbers = [1, 2, 3, 4, 5, 6]
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(f"Even numbers - {evens}")  # Output: [2, 4, 6]

# Sort a list of tuples by the second element
pairs = [(1, 3), (2, 2), (3, 1)]
sorted_pairs = sorted(pairs, key=lambda x: x[1])
print(f"Sorted list {sorted_pairs}")  # Output: [(3, 1), (2, 2), (1, 3)]

# Multiply all numbers in the list
numbers = [1, 2, 3, 4]
product = reduce(lambda x, y: x * y, numbers)
print(f"Multiply - {product}")  # Output: 24