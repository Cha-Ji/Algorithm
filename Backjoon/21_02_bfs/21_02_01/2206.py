# Ex_2206 벽 부수고 이동하기 [골4]
import sys
from collections import deque
N, M = map(int, input().split())
graph = [list(map(int, input())) for _ in range(N)]

dq = deque([[0, 0, 0]])
dist = [[[0] * 2 for __ in range(M)] for _ in range(N)]
dist[0][0][0] = 1

ans = -1
while dq:
    x, y, boom = dq.popleft()
    if x == N-1 and y == M-1:
        ans = dist[x][y][boom]
        break
    for dx, dy in (-1, 0), (1, 0), (0, -1), (0, 1):
        nx = dx + x
        ny = dy + y

        if 0 <= nx < N and 0 <= ny < M:
            # 0
            if graph[nx][ny] == 0 and dist[nx][ny][boom] == 0:
                dist[nx][ny][boom] = dist[x][y][boom] + 1
                dq.append([nx, ny, boom])

            # 1
            elif graph[nx][ny] == 1 and boom == 0 and dist[nx][ny][1] == 0:
                dist[nx][ny][1] = dist[x][y][0] + 1
                dq.append([nx, ny, 1])
print(ans)
