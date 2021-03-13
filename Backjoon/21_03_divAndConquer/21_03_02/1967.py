# Ex_1967 트리의 지름 [골4]
import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
graph = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    l = list(map(int, input().split()))
    graph[l[0]].append([l[1], l[2]])
    graph[l[1]].append([l[0], l[2]])


def bfs(start):
    dq = deque()
    dq.append([start, 0])
    v = [False] * (N + 1)
    maxNode, maxDepth = 0, 0

    while dq:
        node, depth = dq.popleft()
        v[node] = True
        for e, dis in graph[node]:
            if not v[e]:
                v[e] = True
                dq.append([e, dis + depth])

                if dis + depth > maxDepth:
                    maxNode = e
                    maxDepth = dis + depth
    return maxNode, maxDepth


print(bfs(bfs(1)[0])[1])
