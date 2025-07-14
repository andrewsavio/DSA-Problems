# It uses the recursion tree to calculate the fibonacci element

def fibonacci(n: int):
    # here will check for the f(0) and f(1) so if it gives these will return the recursion
    if n <= 1:
        return n
    last = fibonacci(n-1)  # for example if if n=4 then f(n-1) will be 3
    second_last = fibonacci(n-2)  # here f(n-2) will be 2
    # here will add the last and the second last to get the fibonacci element
    return last + second_last
# and here the time complexity is O(2^n) and space complexity is O(n) because of the recursion stack


result = fibonacci(4)
print(result)
