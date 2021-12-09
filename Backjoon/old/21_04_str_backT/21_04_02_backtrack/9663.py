# Ex_9663 N-Queen: [골5]
def isPromising(visitedX, x):
    n = len(visitedX)
    for i in range(n):
        if abs(x - visitedX[i]) == abs(n - i):
            return False
    return True
# 재귀 dfs


def dfs(visitedX, y):
    # 종료조건
    if y == N:
        ans[0] += 1
    else:
        for i in range(N):
            if not visitedY[i] and isPromising(visitedX, i):
                visitedY[i] = True
                dfs(visitedX + [i], y + 1)
                visitedY[i] = False


N = int(input())
ans = [0]
visitedY = [False] * N
dfs([], 0)
print(*ans)
