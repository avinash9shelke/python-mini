#Unpacking Iterables
numbers = [1, 2, 3,4,5,6]
print(*numbers)  # Output: 1 2 3,4,5,6
beginning,*middle,second_last,last=numbers
print(f"first number - {beginning}")
print(f"middle number - {middle}")
print(f"second number - {second_last}")
print(f"last number - {last}")

def add(a, b, c):
    return a + b + c

nums = [1, 2, 3]
print(f"Sum of numbers - {add(*nums)}")  # Output: 6

# Extended Iterable Unpacking
a, *b, c = [1, 2, 3, 4, 5]
print(a)  # 1
print(b)  # [2, 3, 4]
print(c)  # 5

# Using * in List Comprehensions and Function Calls

def multiply(a, b):
    return a * b

pairs = [(2, 3), (4, 5)]
results = [multiply(*pair) for pair in pairs]  # [6, 20]
print(f"Comprehensions results - {results}")

#Merging Lists or Tuples
list1 = [1, 2]
list2 = [3, 4]
merged = [*list1, *list2]  # [1, 2, 3, 4]
print(f"Merged list - {merged}")

