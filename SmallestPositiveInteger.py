class Solution:
    def missingNumber(self, arr):
        # code here
        n = len(arr)

        for i in range(n):
            while 1 <= arr[i] <= n and arr[i] != arr[arr[i]-1]:
                temp = arr[i]
                arr[i] = arr[arr[i]-1]
                arr[temp-1] = temp

        for g in range(1, n+1):
            if g != arr[g-1]:
                return g

        return n+1
