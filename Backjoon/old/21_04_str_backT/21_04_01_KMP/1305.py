# Ex_1305 광고 [플5]
L = int(input())
pat = input()

pi = [0] * L
pref = 0
for suff in range(1, L):
    while pref > 0 and pat[suff] != pat[pref]:
        pref = pi[pref - 1]

    if pat[suff] == pat[pref]:
        pref += 1
        pi[suff] = pref

# 접두사 == 접미사 인 접미사 중 가장 긴 접미사를 떼어내는 문제
print(L - pi[-1])
