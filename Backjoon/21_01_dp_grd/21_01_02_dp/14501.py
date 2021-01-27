# Ex_14501 퇴사: dp [실버4]
import sys
N = int(input())
T = [0]
P = [0]
for i in range(N):
    a,b = list(map(int, sys.stdin.readline().split()))
    T.append(a)
    P.append(b)

dp = [0] * (N + 1)
for i in range(1, N + 1):
    _next = i + T[i] - 1
    dp[i] = max(dp[:i+1])
    if _next <= N:
        dp[_next] = max(dp[_next], P[i] + max(dp[:i]))
print(dp[-1])
