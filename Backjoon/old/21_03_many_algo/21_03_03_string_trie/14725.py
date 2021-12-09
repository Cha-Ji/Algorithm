# Ex_14725 개미굴 [골2]
import sys
input = sys.stdin.readline


class Trie:
    def __init__(self):
        self.head = {}

    def insert(self, feeds):
        cur = self.head

        for feed in feeds:
            if feed not in cur:
                cur[feed] = {}

            cur = cur[feed]
        cur[0] = True

    def search(self, node, floor):
        if 0 in node:
            return

        for child in sorted(node):
            print("-" * floor + child)
            self.search(node[child], floor + 2)


trie = Trie()
for i in range(int(input())):
    trie.insert(input().split()[1:])
trie.search(trie.head, 0)
