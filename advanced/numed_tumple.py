from collections import namedtuple
# Define a namedtuple for a Point in 2D space
Point = namedtuple('Point', ['x', 'y'])

# Function to create a point
def create_point(x, y):
    return Point(x, y)

# Function to calculate distance between two points
def distance(p1, p2):
    return ((p2.x - p1.x)**2 + (p2.y - p1.y)**2)**0.5

# Function to move a point by dx and dy
def move_point(p, dx, dy):
    return Point(p.x + dx, p.y + dy)

# Function to display point nicely
def display_point(p):
    return f"Point(x={p.x}, y={p.y})"

p1 = create_point(2, 3)
p2 = create_point(5, 7)


print("Point 1:", display_point(p1))
print("Point 2:", display_point(p2))
print("Distance:", distance(p1, p2))

p3 = move_point(p1, 1, -1)
print("Moved Point 1:", display_point(p3))




