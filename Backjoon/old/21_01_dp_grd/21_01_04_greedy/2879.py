# 탭 작업에 대한 다른 이해:
# 1. 그룹 평준화
# 2. 그룹 전체 탭

# Ex_2879 코딩은 예쁘게 [골드1]
N = int(input())
thisTab = list(map(int, input().split()))
correctTab = list(map(int, input().split()))

diffTab = [0]*N
for i in range(N):
    diffTab[i] = correctTab[i] - thisTab[i]

tab = diffTab[0]
ans = 0

for i in range(1, N):
    if tab * diffTab[i] < 0:  # 그룹 단체 탭
        ans += abs(tab)
    elif abs(tab) > abs(diffTab[i]):  # 그룹 평준화
        ans += abs(tab - diffTab[i])
    tab = diffTab[i]

print(ans + abs(tab))
