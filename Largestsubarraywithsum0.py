class Solution:
    def maxLength(self, arr):
        # code here
        maxlen = 0
        prefix_sum = 0
        sum_map = {0: -1}
        for i in range(len(arr)):
            prefix_sum += arr[i]
            if prefix_sum in sum_map:
                maxlen = max(maxlen, i-sum_map[prefix_sum])

            else:
                sum_map[prefix_sum] = i
        return maxlen
