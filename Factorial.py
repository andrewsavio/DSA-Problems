def factorial(num):
    if (num == 0):
        return 1
    return num * factorial(num - 1)


result = factorial(3)
print(result)
