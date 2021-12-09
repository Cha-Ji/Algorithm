# Ex_2606 바이러스 [실3]
import sys
from collections import deque
input = sys.stdin.readline

nodeCount = int(input())
E = int(input())

graph = [[]for _ in range(nodeCount + 1)]
for i in range(E):
    a, b = map(int, input().split())

    graph[a].append(b)
    graph[b].append(a)

dq = deque([1])
ans = -1
v = [False] * (nodeCount + 1)
while dq:
    node = dq.popleft()
    if not v[node]:
        v[node] = True
        ans += 1
        for i in graph[node]:
            if not v[i]:
                dq.append(i)

print(ans)
