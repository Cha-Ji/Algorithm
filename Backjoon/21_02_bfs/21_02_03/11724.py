# 연결 요소의 개수 [실2]
import sys
from collections import deque


def bfs(root):
    dq.append(root)
    while dq:
        node = dq.popleft()
        if visted[node]:
            continue
        visted[node] = True
        for i in graph[node]:
            dq.append(i)
    return 1


N, M = map(int, input().split())
graph = [[]for _ in range(N+1)]
visted = [False] * (N + 1)
dq = deque()
ans = 0
for _ in range(M):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)


for i in range(1, N + 1):
    if visted[i]:
        continue
    ans += bfs(i)

print(ans)
