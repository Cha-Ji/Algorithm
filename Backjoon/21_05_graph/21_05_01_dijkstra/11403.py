# Ex_11403 경로 찾기: [실1]

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]

for m in range(N):
    for i in range(N):
        for j in range(N):
            graph[i][j] = graph[i][j] | (graph[i][m] & graph[m][j])

for i in range(N):
    print(*graph[i])
