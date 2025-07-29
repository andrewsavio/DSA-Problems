class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        xor_map = {}
        count = 0
        curr_xor = 0

        for n in A:
            curr_xor ^= n
            if curr_xor == B:
                count += 1

            needed_xor = curr_xor ^ B
            if needed_xor in xor_map:
                count += xor_map[needed_xor]

            if curr_xor in xor_map:
                xor_map[curr_xor] += 1
            else:
                xor_map[curr_xor] = 1
        return count
