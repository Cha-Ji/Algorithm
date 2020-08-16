class Solution:
    def titleToNumber(self, s: str) -> int:
        i = len(s) - 1
        result = 0
        while i >= 0:
            result += (ord(s[i]) - ord("A") + 1) * pow(26, len(s) - i - 1)
            i -= 1
        return result
a = Solution()
print(a.titleToNumber("ZY"))
