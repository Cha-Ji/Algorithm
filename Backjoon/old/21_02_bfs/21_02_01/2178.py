# Ex_2178 미로 탐색 [실1]
import sys
from collections import deque
N, M = map(int, input().split())
maze = [[0] * M for _ in range(N)]

for i in range(N):
    maze[i] = sys.stdin.readline()[:-1]


def canMove(n, m):
    if n < N and m < M and n >= 0 and m >= 0:
        return (not v[n][m]) and (maze[n][m] == '1')
    else:
        return False


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

v = [[False] * M for _ in range(N)]
dist = [[1] * M for _ in range(N)]
q = deque()
q.append([0, 0])
v[0][0] = True

while q:
    i, j = q.popleft()
    for k in range(4):
        nx, ny = i + dx[k], j + dy[k]
        if canMove(nx, ny):
            q.append([nx, ny])
            dist[nx][ny] = dist[i][j] + 1
            v[nx][ny] = True
print(dist[-1][-1])
