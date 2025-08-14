class Solution:
    def isValid(self, s: str) -> bool:
        d = {"(": ")", "{": "}", "[": "]"}
        stack = []
        for c in s:
            if c in d:
                stack.append(c)
            else:
                if stack == [] or d[stack.pop()] != c:
                    return False
        return True if stack == [] else False
