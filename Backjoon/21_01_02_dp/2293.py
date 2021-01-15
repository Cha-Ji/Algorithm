#Ex_2293 동전1 [실버1]
import sys
n, k = list(map(int, input().split()))
coins = [0]*n
dp = [0]*(k+1)
dp[0] = 1
for i in range(n):
    coins[i] = int(sys.stdin.readline())

for coin in coins:
    #  dp[i] : i원을 만드는 경우의 수
    for j in range(k+1):
        if j >= coin:
            dp[j] += dp[j - coin] 
        
print(dp[-1])