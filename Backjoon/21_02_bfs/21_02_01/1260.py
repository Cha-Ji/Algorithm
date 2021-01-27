# Ex_1260 DFS와BFS [실2]
import sys
from collections import deque
import heapq
N, M, V = list(map(int, sys.stdin.readline().split()))

graph = [[]for _ in range(N+1)]  # dfs
graph2 = [[]for _ in range(N+1)]  # bfs

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())

    # dfs
    heapq.heappush(graph[a], b)
    heapq.heappush(graph[b], a)

    # bfs
    heapq.heappush(graph2[a], b)
    heapq.heappush(graph2[b], a)


def dfs(root):
    if not v[root]:
        print(root, end=" ")
        v[root] = True
        while graph[root]:
            dfs(heapq.heappop(graph[root]))


def bfs(root):
    Q = deque()
    Q.append(root)
    v = [False] * (N+1)

    while Q:
        root = Q.popleft()

        if not v[root]:
            v[root] = True
            print(root, end=" ")

            while graph2[root]:
                i = heapq.heappop(graph2[root])
                Q.append(i)


v = [False] * (N+1)
dfs(V)
print()
bfs(V)
