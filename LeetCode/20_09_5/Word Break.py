#실패ㅠ
class Solution:
    def wordBreak(self, s: str, wordDict) -> bool:
        for i in sorted(wordDict, key= lambda x : len(x)):
            print(s)
            s = s.replace(i,"")
        print(s)
        return len(s) == 0
a = Solution()
print(a.wordBreak(s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]))
print(a.wordBreak(s = "leetcode", wordDict = ["leet", "code"]))
print(a.wordBreak(s = "aaaaaaa", wordDict = ["aaaa","aaa"]))
