from ast import List

# This program aims from moving with two pointers


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0
        for r in range(len(nums)):
            if nums[r]:  # here if left = 0 nad and check for if right is not zero
                # if it is not zero then we swap the left and right pointer
                # and move the left pointer to the next element
                nums[left], nums[r] = nums[r], nums[left]
                left += 1  # move the left pointer to the next element
        # After the loop, all non-zero elements are at the beginning of the array
        return nums
