# Problem statement
# Given an integer, check if it is prime or not. Return True if the number is prime, otherwise False.


import math


def check_prime(num: int) -> bool:
    if num <= 1:
        return False
    ctr = 0
    for i in range(1, int(math.sqrt(num))+1):

        if num % i == 0:
            ctr = ctr + 1
            if i != num // i:
                ctr = ctr + 1
    if ctr == 2:
        return True
    else:
        return False
