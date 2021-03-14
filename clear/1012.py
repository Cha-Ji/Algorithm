# Ex_1012 유기농 배추 [실2]
import sys
from collections import deque
input = sys.stdin.readline


def check():
    for i in range(M):
        for j in range(N):
            if graph[i][j] == 1:
                return [i, j]

    return [-1, -1]


for _ in range(int(input())):
    M, N, K = map(int, input().split())
    graph = [[0] * N for _ in range(M)]

    for __ in range(K):
        x, y = map(int, input().split())
        graph[x][y] = 1

    ans = 0

    while True:
        x, y = check()

        if x == -1:
            break

        dq = deque()
        dq.append([x, y])

        while dq:
            x, y = dq.popleft()
            if graph[x][y] == 1:
                graph[x][y] = 0
                for dx, dy in (1, 0), (-1, 0), (0, 1), (0, -1):
                    nx = x + dx
                    ny = y + dy

                    if 0 <= nx < M and 0 <= ny < N and graph[nx][ny] == 1:
                        dq.append([nx, ny])

        ans += 1
    print(ans)
