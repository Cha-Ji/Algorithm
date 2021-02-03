# Ex_1707 이분 그래프 [골4]
import sys
from collections import deque


for _ in range(int(input())):
    # 입력
    V, E = map(int, sys.stdin.readline().split())
    graph = [[]for _ in range(V + 1)]

    for __ in range(E):
        a, b = map(int, sys.stdin.readline().split())
        graph[a].append(b)
        graph[b].append(a)

    # 초기화
    ans = True
    color = [0] * (V + 1)

    # 두 집합(색깔)로 구분이 되면 된다.

    for start in range(1, V + 1):
        if ans == False:
            break
        if color[start] > 0:
            continue

        dq = deque([start])
        color[start] = 1

        while dq and ans:
            node = dq.popleft()

            # 연결된 노드
            for i in graph[node]:
                # 색이 없으면 색칠
                if color[i] == 0:
                    color[i] = 3 - color[node]
                    dq.append(i)

                # 같은 색깔이면 false
                elif color[i] == color[node]:
                    ans = False
                    break

    print("YES" if ans else "NO")
