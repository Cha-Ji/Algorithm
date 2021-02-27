# 3번 땅콩먹기
def main():
    N, M, E = map(int, input().split())
    spot = list(map(int, input().split()))
    dp = [[0]*spot[-1] for _ in range(spot[-1])]

    for i in range(N):
        if i > E:
            break
        startIndex = i

    for i in range(1, E - spot[0]):
        for j in range(1, spot[-1] - E):
            if startIndex - i + j in spot:
                dp[i][j] = max(dp[i][j-1], dp[i-1][j]) + 1
            else:
                dp[i][j] = max(dp[i][j-1], dp[i-1][j])
            if dp[i][j] == M:
                print(i + j)
                return

    """
        왼  1   2   3   4   5   6   7
    오  
    1      m
    2
    3
    4
    5
    6
    7
    """


if __name__ == "__main__":
    main()
