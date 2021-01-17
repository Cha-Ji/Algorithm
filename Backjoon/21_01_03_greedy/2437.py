#Ex_2437 저울 [골드3]
N = int(input())
w = sorted(list(map(int, input().split())))

_sum = 0

# 내가 지금 나타낼 수 있는 수 : 1 ~ sum
# 다음 타겟의 추 + 1 ~ sum 까지 나타낼 수 있다.
# 다음 타겟의 추 + 1 이 sum + 1보다 크다면,
# sum + 1이 답이다.
for i in range(N):
    if _sum + 1 >= w[i]:
        _sum += w[i]
    else:
        break
print(_sum + 1)
