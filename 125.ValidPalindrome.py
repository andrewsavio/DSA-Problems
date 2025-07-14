# This method uses the time complexity of O(n) and space complexity of O(n) to check if a string is a palindrome
# Thiscode uses all the built in functions to check if the string is palindrome or not it akes a bit more memoery than the next program
class Solution:
    def isPalindrome(self, s: str) -> bool:
        NewString = ""
        for c in s:
            if c.isalnum():
                NewString += c.lower()
        return NewString == NewString[::-1]

# This program creates a new function for the finding whether the given string is alphanum or not


class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s)-1
        while l < r:
            while l < r and not self.alphanum(s[l]):
                l += 1
            while r > l and not self.alphanum(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l = l+1
            r = r-1
        return True

    def alphanum(self, c):
        return (ord('A') <= ord(c) <= ord('Z') or ord('a') <= ord(c) <= ord('z') or ord('0') <= ord(c) <= ord('9'))
# the time complexity of this code is O(n) and space complexity is O(1) because it does not use any extra space for storing the string
