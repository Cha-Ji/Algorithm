# Ex_10165 버스 노선 [플1]
import sys
N = int(input())
M = int(input())

dp = [[0, -1]for _ in range(N)]
for i in range(M):
    a, b = map(int, sys.stdin.readline())

    index = min(a, b)
    value = max(a, b)

    if dp[index][0] > 0:
        # 겹치는 것 제거
        True


# 포함 제거
for i in range(M):
    for j in range(i, dp[i]):
        dp[i]
