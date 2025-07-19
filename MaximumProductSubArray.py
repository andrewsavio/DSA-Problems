class Solution:
    def maxProduct(self, arr):
        # code here
        n = len(arr)
        maxProd = float('-inf')

        leftoright = 1
        rightoleft = 1

        for i in range(n):
            if leftoright == 0:
                leftoright = 1
            if rightoleft == 0:
                rightoleft = 1

            leftoright *= arr[i]
            j = n - i - 1
            rightoleft *= arr[j]
            maxProd = max(leftoright, rightoleft, maxProd)

        return maxProd
