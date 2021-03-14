# Ex_17626 Four Squares [실5]
N = int(input())
dp = [4] * (N+1)

for i in range(N):
    if i**2 > N:
        break
    dp[i**2] = 1

    for j in range(i, N):
        if i**2 + j**2 > N:
            break
        dp[i**2 + j**2] = min(dp[i**2 + j**2], 2)

        for k in range(j, N):
            if i**2 + j**2 + k**2 > N:
                break
            dp[i**2 + j**2 + k**2] = min(dp[i**2 + j**2 + k**2], 3)


print(dp[N])
