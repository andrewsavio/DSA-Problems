from ast import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = {}

        for i, num in enumerate(nums):
            # we get a complement when we subtract the number from the target
            complement = target - num
            if complement in num_map:  # Check if the complement is in the map
                # If it is then we return the hashmap with key and its value
                return [num_map[complement], i]
            # else we add the number at its key value in the map
            num_map[num] = i
