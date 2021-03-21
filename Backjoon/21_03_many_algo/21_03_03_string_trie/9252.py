# Ex_9252 LCS2 최장 공통 부분 수열: [골5]
l = ["a" + input(), "b" + input()]
len0 = len(l[0])
len1 = len(l[1])

dp = [[""] * len1 for _ in range(len0)]

for i in range(1, len0):
    for j in range(1, len1):
        if l[0][i] == l[1][j]:
            dp[i][j] = dp[i - 1][j - 1] + l[0][i]
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1], key=lambda x: len(x))

print(len(dp[-1][-1]))
print(dp[-1][-1])
