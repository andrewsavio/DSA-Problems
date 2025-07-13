def findGcd(x, y):
    # Write your code here
    # Return an integer
    while y:
        x, y = y, x % y
    return x
    pass


findGcd(48, 18)  # Example usage
