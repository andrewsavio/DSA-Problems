class Solution:
    def nonRepeatingChar(self, s):
        # code here
        char_count = {}

        for char in s.replace(" ", ""):
            char_count[char] = char_count.get(char, 0)+1

        for char in s.replace(" ", ""):
            if char_count[char] == 1:
                return char

        return '$'
