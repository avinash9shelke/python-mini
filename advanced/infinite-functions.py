
from itertools import count
from itertools import cycle
from itertools import repeat

for i in count(start=10, step=2):
    print(i)
    if i > 20:
        break

colors = ['red', 'green', 'blue']
counter = 0

print('\nStarting the loop \n')

for color in cycle(colors):
    print(color)
    counter += 1
    if counter == 12:
        break

print('\nStarting the loop \n')
for item in repeat('Hello', 3):
    print(item)
