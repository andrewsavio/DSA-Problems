from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        merger = []
        prev = intervals[0]

        for i in range(1, len(intervals)):
            if intervals[i][0] <= prev[1]:
                prev[1] = max(prev[1], intervals[i][1])

            else:
                merger.append(prev)
                prev = intervals[i]

        merger.append(prev)
        return merger
