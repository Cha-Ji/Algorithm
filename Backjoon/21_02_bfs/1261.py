# Ex_1261 알고스팟 [골4]
from collections import deque
import sys
M, N = map(int, input().split())
graph = [list(map(int, sys.stdin.readline()[:-1]))for _ in range(N)]

dist = [[N*M+1]*M for _ in range(N)]  # 뚫은 횟수

dq = deque()
dq.append([0, 0])
dist[0][0] = 0
while dq:
    x, y = dq.popleft()

    for dx, dy in (-1, 0), (1, 0), (0, 1), (0, -1):
        nx = dx + x
        ny = dy + y

        if 0 <= nx < N and 0 <= ny < M:
            if dist[nx][ny] > dist[x][y] + graph[nx][ny]:
                dist[nx][ny] = dist[x][y] + graph[nx][ny]
                dq.append([nx, ny])

print(dist[-1][-1])
