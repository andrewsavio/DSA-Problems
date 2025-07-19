class Solution:
    def circularSubarraySum(self, arr):
        totalSum = 0
        Curr_Max = 0
        Curr_Min = 0
        max_sum = arr[0]
        min_sum = arr[0]

        for i in range(len(arr)):
            Curr_Max = max(Curr_Max+arr[i], arr[i])
            max_sum = max(max_sum, Curr_Max)

            Curr_Min = min(Curr_Min+arr[i], arr[i])
            min_sum = min(Curr_Min, min_sum)

            totalSum += arr[i]
        normalsum = max_sum
        Circularsum = totalSum - min_sum

        if min_sum == totalSum:
            return normalsum

        return max(Circularsum, normalsum)
