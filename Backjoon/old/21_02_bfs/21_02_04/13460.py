# Ex_13460 구슬 탈출2 [골2]
import sys
from collections import deque
input = sys.stdin.readline


def move(x, y, dx, dy):
    while board[x + dx][y + dy] != "#" and board[x][y]:
        x, y = x + dx, y + dy
    return [x, y]


def goBack(nextB, nextR, nowB, nowR, d):
    # 겹치면
    if nextB == nextR and board[nextB[0]][nextB[1]] != "O":
        # 뒤에 있는 공
        if nowB[0] * d[0] < nowR[0] * d[0] or nowB[1] * d[1] < nowR[1] * d[1]:
            nextB[0] -= d[0]
            nextB[1] -= d[1]
        else:
            nextR[0] -= d[0]
            nextR[1] -= d[1]
    return nextB, nextR


def bfs():
    dq = deque()
    dq.append((startB, startR, 0))

    while dq:
        nowB, nowR, count = dq.popleft()
        if board[nowB[0]][nowB[1]] == "O":
            return -1
        if board[nowR[0]][nowR[1]] == "O":
            return count

        for d in (1, 0), (-1, 0), (0, 1), (0, -1):
            nextB = move(nowB[0], nowB[1], d[0], d[1])
            nextR = move(nowR[0], nowR[1], d[0], d[1])
            nextB, nextR = goBack(nextB, nextR, nowB, nowR, d)
            if nextB != nowB or nextR != nowR:
                dq.append((nextB, nextR, count + 1))

        if count > 10:
            return -1
    return -1


N, M = map(int, input().split())
board = [input()[:-1] for _ in range(N)]
for i in range(N):
    for j in range(M):
        if board[i][j] == 'B':
            startB = [i, j]
        elif board[i][j] == 'R':
            startR = [i, j]
print(bfs())
