# Ex_13460 구슬 탈출2 [골2]
import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())

board = [list(input()[:-1])for _ in range(N)]

for i in range(N):
    for j in range(M):
        if board[i][j] == 'B':
            startB = [i, j]

        elif board[i][j] == 'R':
            startR = [i, j]

# 이동 불가할 때 까지 이동


def move(prev, d):
    while True:
        nextBoard = board[prev[0] + d[0]][prev[1] + d[1]]
        if nextBoard == ("#" or "O"):
            break
        else:
            prev[0] += d[0]
            prev[1] += d[1]

    return prev

# 이동 후 위치


def next(prevB, prevR, d):
    # 먼저 이동할 색, 나중에 이동한 색이 같은 곳으로 이동하면 한 칸 뒤로
    bIsFirst = True
    last = 0

    # 동일 축이면 겹치지 않게 조심
    for i in range(2):
        if prevB[i] == prevR[i]:
            #  앞 뒤 순서를 저장 true: b선 false: r선
            bIsFirst = prevB[1-i] > prevR[1-i]
            last = 1

    if bIsFirst:
        nextB = move(prevB, d)
        nextR = move(prevR, d)
        # 쫓아온 색깔은 한칸 뒤로
        if nextB == nextR:
            nextR = [nextR[0] - d[0]*last, nextR[1] - d[1]*last]

    else:
        nextR = move(prevB, d)
        nextB = move(prevR, d)
        # 쫓아온 색깔은 한칸 뒤로, 구멍 빠진건 뒤로 안감
        if nextB == nextR and board[nextB[0]][nextB[1]] != "O":
            nextB = [nextB[0] - d[0]*last, nextB[1] - d[1]*last]

    return nextB, nextR


def bfs():
    dq = deque()
    dq.append((startB, startR, 1))
    vistedR = [[False] * M for _ in range(N)]
    while dq:
        nowB, nowR, count = dq.popleft()
        if board[nowB[0]][nowB[1]] == "O":
            return -1
        if board[nowR[0]][nowR[1]] == "O":
            return count

        for d in (1, 0), (-1, 0), (0, 1), (0, -1):
            nextB, nextR = next(nowB, nowR, d)
            if not vistedR[nowR[0]][nowR[1]]:
                vistedR[nowR[0]][nowR[1]] = True
                dq.append((nextB, nextR, count + 1))

        if count > 10:
            return -1
    return -1


print(bfs())
