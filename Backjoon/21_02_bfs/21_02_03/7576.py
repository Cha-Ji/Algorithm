# Ex_7576 토마토 [실버1]
import sys
from collections import deque
input = sys.stdin.readline


def bfs():
    while dq:
        x, y, day = dq.popleft()

        for dx, dy in (-1, 0), (1, 0), (0, -1), (0, 1):
            nx = dx + x
            ny = dy + y
            print(ny)
            if 0 <= nx < N and 0 <= ny < M:
                if box[nx][ny] == 0:
                    dq.append([nx, ny, day + 1])
                    box[nx][ny] = 1
    for result in box:
        if 0 in result:
            return -1
    return day


M, N = map(int, input().split())
box = []
dq = deque()

for i in range(N):
    box.append(list(map(int, input().split())))

    for j in range(M):
        if box[i][j] == 1:
            dq.append([i, j, 0])

print(bfs())
