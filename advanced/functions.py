# Function definition with parameters
def greet(name, message):
    print(f"Hello {name}, {message}")
# Function call with arguments
greet("Avinash", "welcome to the Python world!")

# -------------------------------------------------------------

# Positional Arguments

def add(a, b):
    return a + b

print(f"Positional Arguments Example - {add(5, 3)}")  # Output: 8

# -------------------------------------------------------------

#Keyword Arguments
print(f"Keyword Arguments Example - {add(b=3, a=5)}")  # Output: 8

# -------------------------------------------------------------

#Default Arguments
def greet(name, message="Good morning"):
    print(f"Hello {name}, {message}")

greet("Avinash")  # Uses default message

# -------------------------------------------------------------

#Variable-length Arguments

#*args - for non-keyword variable arguments
#**kwargs  - for keyword variable arguments

def show_args(*args, **kwargs):
    print("Args:", args)
    print("Kwargs:", kwargs)

show_args(1, 2, 3,'a', name="Avinash", role="Engineer")

# -------------------------------------------------------------

def describe_person(name, *hobbies, **details):
    print(f"Name: {name}")
    print("Hobbies:", hobbies)
    print("Details:")
    for key, value in details.items():
        print(f"  {key}: {value}")

describe_person(
    "Avinash",
    "Reading", "Cycling",
    age=30, city="Pune", profession="Engineer"
)

# -------------------------------------------------------------

#Unpacking in Function Arguments

def add(a, b, c):
    return a + b + c

values = [10, 20, 30]
print(f"\nUnpacking in Function Arguments - {add(*values)}")  # Output: 60

# -------------------------------------------------------------

#Global and Local Variable Example

# Global variable
message = "Hello from global scope"

def greet():
    # Local variable
    message = "Hello from local scope"
    print("Inside function:", message)

greet()
print("Outside function:", message)

# -------------------------------------------------------------

#Modifying Global Variable Inside a Function

count = 0  # Global variable

def increment():
    global count  # Declare that we want to use the global variable
    count += 1

increment()
print("Count after increment:", count)

# -------------------------------------------------------------

#Immutable Type (Pass-by-value-like behavior)

def modify_number(x):
    x = x + 10
    print("Inside function:", x)

num = 5
modify_number(num)
print("Outside function:", num)

# -------------------------------------------------------------

#Mutable Type (Pass-by-reference-like behavior)

def modify_list(lst):
    lst.append(100)
    print("Inside function:", lst)

my_list = [1, 2, 3]
modify_list(my_list)
print("Outside function:", my_list)