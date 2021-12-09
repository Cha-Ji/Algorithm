# Ex_2533 사회망 서비스(SNS) [골3]
# (독립집합) => 모든 원소가 서로 인접해있지 않은 집합
import sys
from collections import deque

input = sys.stdin.readline


def setChild():
    stack = [1]
    child = []  # 탐색 순서

    for _ in range(N):
        root = stack.pop()
        child.append(root)
        v[root] = True
        for node in tree[root]:
            if not v[node]:
                stack.append(node)
    return child


# 입력
N = int(input())
tree = [[] * (N + 1) for _ in range(N + 1)]

for _ in range(N - 1):
    u, v = map(int, input().split())
    tree[u].append(v)
    tree[v].append(u)

v = [False] * (N + 1)
dp = [[1, 0] for _ in range(N + 1)]  # 독립집합 개수 dp, [나 포함, 미포함]
child = setChild()

# 독립집합을 뺀 나머지가 얼리어답터.
while child:
    root = child.pop()
    v[root] = False
    for node in tree[root]:
        if not v[node]:
            dp[root][0] += dp[node][1]
            dp[root][1] += max(dp[node])


print(N - max(dp[1]))
