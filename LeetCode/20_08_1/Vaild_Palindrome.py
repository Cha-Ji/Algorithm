# 2020.08.05_August Challenge
# palindrome : 회문
class Solution:
    def checkAscii(self,str) -> bool:    # only upper
        if 48 <= ord(str) <= 57:
            return False
        elif 65 <= ord(str) <= 90:
            return False
        else:
            return True

    def isPalindrome(self, s: str) -> bool:
        s = s.upper()
        for i in s:
            if self.checkAscii(self.i):
                s = s.replace(i, "").strip()
        return s == s[::-1]
print(Solution.isPalindrome(Solution,"A man, a plan, a canal: Panama"))

