#Ex_11047 동전0 greedy [실버1]
N, K = list(map(int, input().split()))

c = [0] * N
for i in range(N):
    c[i] = int(input())

ans = 0
for coin in c[::-1]:
    while K >= coin:
        K -= coin
        ans += 1

print(ans)