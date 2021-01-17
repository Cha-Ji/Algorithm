# Ex_14501 퇴사: dp [실버4] 리팩토링
import sys
N = int(input())
dp = [0] * (N + 1)
for i in range(1, N + 1):
    T,P=list(map(int,sys.stdin.readline().split()))
    n=i+T-1
    dp[i]=max(dp[i],dp[i-1])
    if n<=N:
        dp[n] = max(dp[n], P + dp[i])
print(dp[-1])
