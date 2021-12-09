# Ex_1701 Cubeditor [골2]
target = input()
ans = 0
for i in range(len(target)):
    pat = target[i:]
    pi = [0] * (len(pat) + 1)

    pref = 0
    for suff in range(1, len(pat)):
        while pref > 0 and pat[suff] != pat[pref]:
            pref = pi[pref - 1]

        if pat[suff] == pat[pref]:
            pref += 1
            pi[suff] = pref
    ans = max(ans, max(pi))

print(ans)
