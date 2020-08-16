from itertools import combinations
class CombinationIterator:
    def __init__(self, characters: str, combinationLength: int):
        self.cList = list(combinations(characters,combinationLength))
        self.resultList = []

        for i in self.cList:
            element = ""
            for j in range(len(i)):
                element += i[j]
            self.resultList.append(element)
        self.resultList.reverse()
    def next(self) -> str:
        return self.resultList.pop()

    def hasNext(self) -> bool:
        return len(self.resultList) > 0

a = CombinationIterator("abc",2)
print(a.resultList)


