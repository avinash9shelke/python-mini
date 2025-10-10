fruits = ["apple", "banana", "cherry", "mango"]
print(fruits)
fruits.append("orange")
print(fruits)

fruits.insert(1, "kiwi")
print(fruits)

fruits.remove("banana")
print(fruits)

last_fruit = fruits.pop()
print(f"pop the element from list - {last_fruit}")

print(fruits)

fruits.sort()

print(f"After sorting the list  - {fruits}")

fruits.reverse()
print(f"After reverse the list  - {fruits}")

position = fruits.index("cherry")
print(f"The position of cherry is - {position}")

