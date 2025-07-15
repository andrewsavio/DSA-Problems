from ast import List

# In this program what we do is
# We put for loop till the len of the array and then compare the first element with the next element
# If the the next element is smaller for the first lemetn then count goes one the problem is the count if it goes more than 1
# Then it is not srted and rotated array
# Then we return False
# Otherise at the end of the loop we return True


class Solution:
    def check(self, nums: List[int]) -> bool:
        count = 0
        n = len(nums)

        for i in range(n):
            if nums[i] > nums[(i+1) % n]:
                count = count+1
            if count > 1:
                return False
        return True
