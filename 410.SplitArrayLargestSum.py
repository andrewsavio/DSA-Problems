from typing import List


class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        low, high = max(nums), sum(nums)
        ans = high
        while low <= high:
            mid = (low+high)//2
            if self.is_feasible(nums, mid, k):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans

    def is_feasible(self, nums, max_sum, k):
        count = 1
        curr_Sum = 0
        for num in nums:
            curr_Sum += num
            if curr_Sum > max_sum:
                count += 1
                curr_Sum = num
                if count > k:
                    return False
        return True
