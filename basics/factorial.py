def factorial(number):
    if number == 0:
        return 1
    elif number > 1:
        return number * factorial(number - 1)
    else:
        return 0


inputValue = int(input('Enter the number : '))
print(f"Factorial of the {inputValue} is {factorial(inputValue)}")
