import array


def ispalindrome(s: str, i: int = 0, n: int = -1):
    if n == -1:
        n = len(s)
    if i >= n // 2:
        return True
    if s[i] != s[n - i - 1]:
        return False
    return ispalindrome(s, i + 1, n)


string = "madam"
result = ispalindrome(string)

print(result)
