class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        for i in range(ord('a'), ord('z')):
            if s.count(chr(i)) != t.count(chr(i)):
                return chr(i)

a = Solution()
print(a.findTheDifference('abcd', 'abcde'))
