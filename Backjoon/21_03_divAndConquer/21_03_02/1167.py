# Ex_1167 트리의 지름 [골3]
from collections import deque


N = int(input())
tree = [[] for _ in range(N + 1)]

for _ in range(N):
    l = list(map(int, input().split()))[:-1]
    for i in range(1, len(l), 2):
        tree[l[0]].append([l[i], l[i+1]])


def bfs(root):
    dq = deque()
    dq.append([root, 0])
    visited = [False] * (N + 1)
    visited[root] = True

    maxNode, maxDis = 0, 0
    while dq:
        node, dis = dq.popleft()
        for v, e in tree[node]:
            if not visited[v]:
                visited[v] = True
                dq.append([v,  dis + e])

                # 최대값 갱신
                if dis + e > maxDis:
                    maxNode = v
                    maxDis = dis + e
    return maxNode, maxDis


# 임의의 노드 x에서 가장 먼 노드 y는 지름의 두 정점 중 하나이다.
print(bfs(bfs(1)[0])[1])
