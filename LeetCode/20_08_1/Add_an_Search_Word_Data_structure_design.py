class Node:
    def __init__(self):
        self.child = {}
        self.endMark = False

class WordDictionary:
    def __init__(self):
        self.wordDict = Node()

    def addWord(self, word: str) -> None:
        root = self.wordDict
        for i in word:
            root = root.child.setdefault(i, Node())
        root.endMark = True

    def searchTree(self, node, word, i):
        if i == len(word): return node.endMark

        if word[i] == ".":
            for all in node.child:
                if self.searchTree(node.child[all], word, i+1): return True

        if word[i] in node.child:
            return self.searchTree(node.child[word[i]], word, i+1)

    def search(self, word: str) -> bool:
        return self.searchTree(self.wordDict, word, 0)

test = WordDictionary()
test.addWord("and")
print(test.search("a.d"))

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
