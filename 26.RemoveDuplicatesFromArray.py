# This program aims with an exmaple of num= [1, 1, 2, 2, 3]
# to remove the duplicates from the array we have two pointers
# one pointer fo from 0 and the another pointer goes from 1

from ast import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        j = 0
        for i in range(1, len(nums)):
            # We compare whether the crrent element is not equal to the previous element
            if nums[j] != nums[i]:
                j += 1  # if num = [1, 1, 2, 2, 3] then j will move to 1
            # If it is not equal then we move the j pointer to the next element
            # and we put the current element at that position
                nums[j] = nums[i]
        return j+1
