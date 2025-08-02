from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1
        while left <= right:
            mid_index = (left+right) // 2
            mid = nums[mid_index]
            if mid > target:
                right = mid_index - 1
            elif mid < target:
                left = mid_index + 1
            elif mid == target:
                return mid_index
        return -1
