#Ex_11053 가장 긴 증가하는 부분 수열 [실버2]
import sys
N = int(input())

S = list(map(int,input().split()))

dp = [1]*N
for now in range(1, N):
    for prev in range(0, now):
        if S[now] > S[prev]:
            dp[now] = max(dp[now], dp[prev] + 1)
print(max(dp))


