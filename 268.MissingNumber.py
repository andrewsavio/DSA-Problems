class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = len(nums)

        for i in range(len(nums)):
            res += (i - nums[i])
        return res
# The progrma is to find the missing number in the aray by looping
# First thourgh the array and adding the length of the array to the result
# Then we loop through the array and subtract the index from the value at that index
# Finally, we return the result which will be the missing number in the array
        # If the array is empty then we return 0
