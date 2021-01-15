#Ex_11399 ATM 그리디 [실버3]
N = int(input())
P = sorted(list(map(int, input().split())))

ans = 0
for i in range(N):
    ans += (N-i)*P[i]
print(ans)
