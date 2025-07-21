class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = ""
        carry = 0
        a, b = a[::-1], b[::-1]

        for i in range(max(len(a), len(b))):
            digit1 = ord(a[i]) - ord("0") if i < len(a) else 0
            digit2 = ord(b[i]) - ord("0") if i < len(b) else 0

            total = digit1 + digit2 + carry
            char = str(total % 2)
            res = char + res

            carry = total // 2

        if carry:
            res = '1' + res

        return res.lstrip('0') or '0'
