# Ex_13549 숨바꼭질3 [골5]
N, K = map(int, input().split())
ans = [float('inf')] * 100001
ans[N] = 1

for i in range(N):
    ans[i] = N - i + 1

for j in range(1, 99999):
    ans[j] = min(ans[j - 1] + 1, ans[j + 1] + 1, ans[j])
    for i in range(100001):
        spot = j * pow(2, i)
        if spot > 100000:
            break
        ans[spot] = min(ans[j], ans[spot])

print(ans[K])
