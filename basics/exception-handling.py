def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError as e:
        print(f"Failed due to - {e}")
    else:
        print("result is", result)
    finally:
        print("executing finally clause")

divide(100,100)
divide(100,0)