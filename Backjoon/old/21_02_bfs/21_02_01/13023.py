# Ex_13023 ABCDE [골5]
import sys

# dfs


def dfs(root, depth):
    global ans
    if depth >= 4:
        ans = 1
        return

    v[root] = True
    for node in graph[root]:
        if not v[node]:
            dfs(node, depth + 1)
            v[node] = False


# 입력
N, M = map(int, input().split())
graph = [[]for _ in range(N)]
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

v = [False for _ in range(N)]

ans = 0
for i in range(N):
    dfs(i, 0)
    v[i] = False

print(ans)
