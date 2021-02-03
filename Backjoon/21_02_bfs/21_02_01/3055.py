# Ex_3055 탈출 [골5]
import sys
from collections import deque


def bfs(x, y, item, d):
    dq = deque()
    dq.append([x, y])
    d[x][y] = 0
    while dq:
        x, y = dq.popleft()
        if item == "S" and graph[x][y] == 'D':
            return

        # 이동
        for dx, dy in (-1, 0), (1, 0), (0, -1), (0, 1):
            nx = x + dx
            ny = y + dy

            if 0 <= nx < R and 0 <= ny < C:
                if item == "S":
                    # 홍수보다 빠르고
                    if waterDist[nx][ny] > dist[x][y] + 1:
                        # 빈 곳이나 목적지일 때
                        if graph[nx][ny] == "D" or graph[nx][ny] == ".":
                            if d[x][y] + 1 < d[nx][ny]:
                                d[nx][ny] = d[x][y] + 1
                                dq.append([nx, ny])

                else:
                    # 빈 곳일 때
                    if graph[nx][ny] == ".":
                        if d[x][y] + 1 < d[nx][ny]:
                            d[nx][ny] = d[x][y] + 1
                            dq.append([nx, ny])

                        # 초기화
R, C = map(int, input().split())
graph = [0 for _ in range(R)]

waterList = []

INF = 99999999
dist = [[INF - 1]*C for _ in range(R)]
waterDist = [[INF]*C for _ in range(R)]

# 입력
for i in range(R):
    graph[i] = sys.stdin.readline()[:-1]

for i in range(R):
    for j in range(C):
        # 출발지점
        if 'S' == graph[i][j]:
            startX, startY = i, j

        # 종료지점
        if 'D' == graph[i][j]:
            endX, endY = i, j

        # 홍수지점
        if '*' == graph[i][j]:
            waterList.append([i, j])

# 홍수
for waterX, waterY in waterList:
    bfs(waterX, waterY, "*", waterDist)

# 이동
bfs(startX, startY, "S", dist)

print('KAKTUS' if dist[endX][endY] == INF - 1 else dist[endX][endY])
