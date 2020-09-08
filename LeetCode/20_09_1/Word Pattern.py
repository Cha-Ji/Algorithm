class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        word_list = str.split()
        if len(word_list) != len(pattern):
            return False
        pattern_dict = {}
        str_dict = {}
        for i in range(len(pattern)):
            try:
                if str_dict[word_list[i]] != pattern[i]:
                    return False
            except:
                str_dict[word_list[i]] = pattern[i]
            try:
                if pattern_dict[pattern[i]] != word_list[i]:
                    return False
            except:
                pattern_dict[pattern[i]] = word_list[i]
        return True
a = Solution()
print(a.wordPattern("aaaa","dog dog dog dog"))
