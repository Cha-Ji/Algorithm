# Ex_1799 비숍: [골2]


def dfs(diffXY, cnt):
    # y - x로 대각선 그룹을 나눈다.
    # 우상단 => 좌하단
    if abs(diffXY) < N:
        ans[0] = max(ans[0], cnt)

        # 현재 대각선 요소 중 하나 방문
        # v = 반대방향 대각선 방문
        for x in range(max(0, - diffXY), min(N, N - diffXY)):
            y = diffXY + x
            if board[x][y] == 1 and not v[x + y]:
                v[x + y] = True
                dfs(diffXY + 1, cnt + 1)
                v[x + y] = False
        dfs(diffXY + 1, cnt)

# def dfs():
#     stack = []
#     diff = -N + 1
#     stack.append([diff, []])

#     while abs(diff) < N:
#         diff, v = stack.pop()
#         ans[0] = max(ans[0], len(v))

#         stack.append([diff + 1, v])
#         for x in range(max(0, - diff), min(N, N - diff)):
#             y = diff + x
#             if board[x][y] == 1 and x + y not in v:
#                 stack.append([diff + 1, v + [x + y]])




N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
v = [False] * 2 * N
ans = [0]

dfs()
print(ans)
