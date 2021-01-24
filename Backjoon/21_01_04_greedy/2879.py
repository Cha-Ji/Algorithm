# Ex_2879 코딩은 예쁘게 [골드1]
N = int(input())
thisTab = list(map(int, input().split()))
correctTab = list(map(int, input().split()))

diffTab = [0]*N
for i in range(N):
    diffTab[i] = correctTab[i] - thisTab[i]

# 그룹 중 가장 작은 수를 일괄 차감
group = []

# 차감 후 안에서 다시 그룹화
