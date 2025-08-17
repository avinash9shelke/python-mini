# Global scope
x = 10

def outer_function():
    # Enclosing scope
    y = 20

    def inner_function():
        # Local scope
        z = 30
        print("x (global):", x)
        print("y (enclosing):", y)
        print("z (local):", z)

    inner_function()

outer_function()

# Accessing z outside its scope will raise an error
# print(z)  # Uncommenting this will cause a NameError
