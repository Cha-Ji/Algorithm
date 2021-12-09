# Ex_11404 플로이드: [골4]

n = int(input())
graph = [[float('inf')] * (n + 1) for _ in range(n + 1)]
for i in range(int(input())):
    # 버스의 시작 도시 a, 도착 도시 b, 한 번 타는 비용 c
    a, b, c = map(int, input().split())
    graph[a][b] = min(graph[a][b], c)

for mid in range(1, n + 1):
    for start in range(1, n + 1):
        for end in range(1, n + 1):
            if start == end:
                graph[start][end] = 0
            
            elif graph[start][end] > graph[start][mid] + graph[mid][end]:
                graph[start][end] = graph[start][mid] + graph[mid][end]

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if graph[i][j] >= float('inf'):
            graph[i][j] = 0
        print(graph[i][j], end = ' ')
    print()