from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        l, r = 0, len(matrix)-1
        while l < r:
            for i in range(r-l):
                top, bottom = l, r

                # 1
                topleft = matrix[top][l+i]
                # 2
                matrix[top][l+i] = matrix[bottom-i][l]
                # 3
                matrix[bottom-i][l] = matrix[bottom][r-i]
                # 4
                matrix[bottom][r-i] = matrix[top+i][r]
                # 5
                matrix[top+i][r] = topleft
            l += 1
            r -= 1

# Example usage:
# solution = Solution()
# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# solution.rotate(matrix)
# print(matrix)  # Output: [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
