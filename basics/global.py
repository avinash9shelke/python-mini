x =10
def my_function():
    global y
    y = 100
    print(f"Scope value of x is {x}")

my_function()
print(f"Global value of y is {y}")