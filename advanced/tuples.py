# Tuples is an immutable collection with maintain order and allow duplicate elements.

person = ("Avinash", 35, "Engineer", "Pune")
no_of_elements = person.count("Engineer")
print(f"No of elements are {no_of_elements}")

index_of_engineer = person.index("Engineer")
print(f"Index of Engineer is {index_of_engineer}")

#Tuple unpacking – Assigning tuple elements to variables
name, age, job, city = person
print(f"Name is {name}, Age is {age}, Job is {job} and City is {city}")

#Slicing – Accessing parts of the tuple
print(f"First and third elements are {person[1:3]}")
print(f"Last three elements are {person[-3:]}")

#Example Demonstrating Tuple Immutability

# Creating a tuple
colors = ("red", "green", "blue")

print(f"Original tuple is {colors}")

# TypeError: 'tuple' object does not support item assignment
# colors[3] = "yellow"
# print(f"Modified tuple is {colors}")

#Concatenate tuples

new_colors = colors + ("yellow",) # it'd create a new tuple with added value and does not modify the existing tuple.
print(f"New tuple is {new_colors}")
print(f"Existing tuple is {colors}")

#Tuples with Mutable Elements

# Note: Tuples themselves are immutable, but they can contain mutable elements like lists:
mixed = (1, [2, 3], 4)
mixed[1][0] = 99
#Here, the tuple structure is unchanged, but the list inside it was modified.
print(f"Mixed tuple is {mixed}")

