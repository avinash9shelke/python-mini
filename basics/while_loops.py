number = int(input("Enter the number:"))
result = 1
while number>0:
    result = result * number
    number  = number - 1

print(f"Factorial of {number} is {result}")
