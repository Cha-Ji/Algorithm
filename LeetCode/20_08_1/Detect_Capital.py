class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if len(word) == 1:
            return True
        return (word == word.upper() or word[1:].islower())
print(Solution.detectCapitalUse(Solution,"U"))
