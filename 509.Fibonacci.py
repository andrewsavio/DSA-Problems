class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        a, b = 0, 1
        for i in range(2, n+1):
            a, b = b, a+b
        return b
# The time complexity of this code is O(n) and space complexity is O(1) because it uses only a constant amount of space


result = Solution().fib(4)
print(result)
# This program uses an iterative approach to calculate the nth Fibonacci number
