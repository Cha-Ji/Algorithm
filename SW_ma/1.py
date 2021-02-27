import sys
from collections import deque
input = sys.stdin.readline


def main():
    skill = input().split()
    N = int(input())
    graph = [[]for _ in range(ord('z') - ord('A') + 1)]

    def bfs(start, startAlpha):
        dq = deque([[start, startAlpha]])
        v = [False] * (ord('z') - ord('A') + 1)
        check = False
        while dq:
            root, result = dq.popleft()

            v[root] = True

            for node in graph[root]:
                if not v[node]:
                    dq.append([[node, result + " " + chr(node + 65)]])
                    check = True
            if check == False:
                print(result)

    for i in range(N):
        x, y = input().split()
        x = ord(x) - ord('A')
        y = ord(y) - ord('A')
        graph[x].append(y)
        graph[y].append(x)

    for i in skill:
        print(bfs(ord(i) - ord('A'), i))


if __name__ == "__main__":
    main()
