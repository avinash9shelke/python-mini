import copy

# Shallow Copy Example

original = [[1, 2], [3, 4]]
shallow = copy.copy(original)

# Modify the nested list
shallow[0][0] = 99

print("Original:", original)
print("Shallow Copy:", shallow)

# Deep Copy Example
original = [[1, 2], [3, 4]]
deep = copy.deepcopy(original)

# Modify the nested list
deep[0][0] = 99

print("Original:", original)
print("Deep Copy:", deep)

