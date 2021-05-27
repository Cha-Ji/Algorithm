# Ex_1799 비숍: [골2]
def dfs(i, count, wb):
    if i >= N + wb:
        return

    ans[0] = max(ans[0], count)

    if wb == 0:
        canVisit = white
    else:
        canVisit = black

    for x, y in canVisit[i]:
        if not visited[x - y + N]:
            visited[x - y + N] = True
            dfs(i + 1, count + 1, wb)
            visited[x - y + N] = False
    # 미방문
    dfs(i + 1, count, wb)


N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
visited = [False] * 2 * N
white = [[] for _ in range(N + 1)]
black = [[] for _ in range(N + 1)]

for x in range(N):
    for y in range(N):
        if board[x][y] == 1:
            if (x + y) % 2 == 0:
                white[(x + y)//2].append([x, y])
            else:
                black[(x + y)//2].append([x, y])

ans = [0]
dfs(0, 0, 0)
dfs(0, ans[0], 1)

print(*ans)

