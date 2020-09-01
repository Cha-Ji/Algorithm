class Solution:
    def toGoatLatin(self, S: str) -> str:
        inputList = S.split()

        index = 2
        for i in range(len(inputList)):
            if inputList[i][0] in ['a','e','i','o','u','A','E','O','U','I']:
                inputList[i] += "m" + "a" * index
            else:
                inputList[i] = inputList[i][1:] + inputList[i][0] + "m" + "a" * index
            index += 1
        result = ""
        for i in inputList:
            result += i + " "

        return result[:-1]
a = Solution()
print(a.toGoatLatin("I speak Goat Latin"))
