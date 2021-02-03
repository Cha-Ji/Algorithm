# Ex_3055 탈출 [골5]
import sys
from collections import deque


# 움직일 수 있는지 검사


def canMove(x, y):
    if 0 <= x < R and 0 <= y < C:
        return (graph[x][y] != '*'
                and graph[x][y] != 'X'
                )
    else:
        return False


def canMoveWater(x, y):
    if 0 <= x < R and 0 <= y < C:
        return (graph[x][y] != 'D'
                and graph[x][y] != 'X'
                and graph[x][y] != 'S')
    else:
        return False


def bfs(x, y):

    dq = deque()
    dq.append([x, y])
    dist[x][y] = 0

    while dq:
        x, y = dq.popleft()
        if graph[x][y] == 'D':
            return

        # 이동
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if canMove(nx, ny) and waterDist[nx][ny] > dist[x][y] + 1:
                if dist[x][y] + 1 < dist[nx][ny]:
                    dist[nx][ny] = dist[x][y] + 1

                    dq.append([nx, ny])


def waterDfs(x, y):
    dq = deque()
    dq.append([x, y])
    waterDist[x][y] = 0
    # 이동
    while dq:
        x, y = dq.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if canMoveWater(nx, ny):
                if waterDist[x][y] + 1 < waterDist[nx][ny]:
                    waterDist[nx][ny] = waterDist[x][y] + 1

                    dq.append([nx, ny])


# 초기화
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

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
for i, j in waterList:
    waterDfs(i, j)

# 이동
bfs(startX, startY)

print('KAKTUS' if dist[endX][endY] == INF - 1 else dist[endX][endY])
