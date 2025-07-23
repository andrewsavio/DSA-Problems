class Solution:
    def maxSum(self, arr):
        # code here
        maxsum = 0
        for i in range(len(arr)-1):
            a, b = arr[i], arr[i+1]
            if a < b:
                min1, min2 = a, b
            else:
                min1, min2 = b, a
            maxsum = max(maxsum, min1+min2)
        return maxsum
