from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sub_num = {0: 1}
        total = count = 0
        for i in nums:
            total += i
            if total-k in sub_num:
                count += sub_num[total-k]

            sub_num[total] = 1+sub_num.get(total, 0)
        return count
