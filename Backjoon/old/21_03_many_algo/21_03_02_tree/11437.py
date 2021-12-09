# Ex_11437 LCA [골3]
import sys
from collections import deque
input = sys.stdin.readline
INF = sys.maxsize


def beHighNode(root, targetDepth):
    for _ in range(targetDepth):
        for node in graph[root]:
            if depth[node] < depth[root]:
                root = node
                break
    return root


def parent(a, b):  # 공통 조상을 알아내는 함수

    lowNode = max(a, b, key=lambda x: (depth[x], x))
    highNode = min(a, b, key=lambda x: (depth[x], x))

    # 같은 깊이가 될 때 까지 올라간다.
    lowNode = beHighNode(lowNode, depth[lowNode] - depth[highNode])

    # 서로 만날때까지 같이 올라간다.
    while lowNode != highNode:
        lowNode = beHighNode(lowNode, 1)
        highNode = beHighNode(highNode, 1)

    return lowNode


N = int(input())

graph = [[] * (N + 1) for _ in range(N + 1)]
depth = [INF] * (N+1)
depth[1] = 0
for _ in range(N-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 트리 문제는 입력을 다 받아야 부모 자식 관계를 알 수 있다.
dq = deque()
dq.append(1)
while dq:
    root = dq.popleft()
    for node in graph[root]:
        if depth[node] == INF:
            depth[node] = depth[root] + 1
            dq.append(node)

for _ in range(int(input())):
    a, b = map(int, input().split())
    print(parent(a, b))
