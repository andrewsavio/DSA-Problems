from typing import List


class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pi = 0
        ni = 1
        res = [0] * len(nums)
        for i in nums:
            if i > 0:
                res[pi] = i
                pi += 2
            else:
                res[ni] = i
                ni += 2
        return res
