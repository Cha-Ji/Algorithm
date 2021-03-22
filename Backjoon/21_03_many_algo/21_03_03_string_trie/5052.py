# Ex_5052 전화번호 목록 [골4]
import sys
input = sys.stdin.readline


class Node():
    def __init__(self):
        self.child = [-1] * 10


class Trie():
    def __init__(self):
        self.head = Node()

    def insert(self, phoneNum):
        cur = self.head

        for num in phoneNum:
            num = int(num)
            if cur.child[num] == -1:
                cur.child[num] = Node()
            cur = cur.child[num]

        # 끝맺음
        cur.child[num] = -2

    def search(self, phoneNum):
        cur = self.head

        for num in phoneNum:
            num = int(num)

            if -2 in cur.child:
                return False

            cur = cur.child[num]
        return True


for _ in range(int(input())):
    trie = Trie()

    n = int(input())
    phoneBook = [input()[:-1] for _ in range(n)]

    for num in phoneBook:
        trie.insert(num)

    ans = "YES"
    for num in phoneBook:
        if not trie.search(num):
            ans = "NO"

    print(ans)
