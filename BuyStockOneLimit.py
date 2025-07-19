class Solution:
    def maximumProfit(self, prices):
        # code here
        res = 0
        min_soFar = prices[0]

        for i in range(len(prices)):
            min_soFar = min(min_soFar, prices[i])

            res = max(res, prices[i]-min_soFar)

        return res
