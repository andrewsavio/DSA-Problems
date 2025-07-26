from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        N = set(nums)
        longest = 0
        for n in N:
            if (n-1) not in N:
                length = 0
                while (n+length) in N:
                    length += 1
                longest = max(length, longest)
        return longest
