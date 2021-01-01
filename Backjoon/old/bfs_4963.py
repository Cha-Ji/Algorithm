from collections import deque
def bfs(graph, start):
    queue = deque([start])

    #     상  하  좌  우 좌상 좌하 우상 우하
    dx = [-1, 1, 0, 0, -1,  1, -1,  1]
    dy = [0, 0, -1, 1, -1, -1,  1,  1]

    # 인접행렬 모두 탐험
    while queue:
        v = queue.popleft()
        graph[v[0]][v[1]] = 0

        # 8방향으로 탐색
        for i in range(8):

            #방문 체크
            x = v[0] + dx[i]
            y = v[1] + dy[i]

            # 벗어나면 
            if x < 0 or y < 0 or \
                x >= len(graph) or y >= len(graph[0]):
                continue

            elif graph[x][y] == 1:
                queue.append([x,y])
                graph[x][y] = 0


while True:
    w, h = map(int, input().split())
    ans = 0
    # 0 0 이 입력되면 종료
    if w == 0 and h == 0:break

    # 그래프를 입력받는다.
    graph = [[0]]*h
    for i in range(h):
        graph[i] = list(map(int, input().split()))

    
    # 땅을 찾는다.
    for i in range(len(graph)):
        for j in range(len(graph[i])):
            if graph[i][j] == 1:
                bfs(graph, [i,j])
                ans += 1
    print(ans)

