from collections import deque


# Function to create a deque from a list
def create_deque(items):
    return deque(items)


# Function to add items to both ends
def add_items(dq, front=None, back=None):
    if front is not None:
        dq.appendleft(front)
    if back is not None:
        dq.append(back)
    return dq


# Function to remove items from both ends
def remove_items(dq, from_front=True, from_back=True):
    if from_front and dq:
        dq.popleft()
    if from_back and dq:
        dq.pop()
    return dq


# Function to rotate the deque
def rotate_deque(dq, steps):
    dq.rotate(steps)
    return dq


# Function to display the deque
def display_deque(dq):
    print("Deque contents:", list(dq))


items = ['a', 'b', 'c']
dq = create_deque(items)

print("Original deque:")
display_deque(dq)

print("\nAfter adding 'x' to front and 'y' to back:")
add_items(dq, front='x', back='y')
display_deque(dq)

print("\nAfter removing from both ends:")
remove_items(dq)
display_deque(dq)

print("\nAfter rotating by 2 steps:")
rotate_deque(dq, 2)
display_deque(dq)
