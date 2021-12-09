# Ex_1916 최소비용 구하기: [골5]
import heapq


def dijkstra(start, end):
    stoe = [float('inf')] * (N + 1)
    stoe[start] = 0

    mid = [[0, start]]

    while mid:
        midWeight, midNode = heapq.heappop(mid)

        for endWeight, endNode in graph[midNode]:
            if midWeight + endWeight < stoe[endNode]:
                stoe[endNode] = midWeight + endWeight
                heapq.heappush(mid, [stoe[endNode], endNode])

    return stoe[end]


N = int(input())
M = int(input())
graph = [[] * (N + 1) for _ in range(N + 1)]

for _ in range(M):
    s, e, w = map(int, input().split())
    graph[s].append([w, e])

s, e = map(int, input().split())
print(dijkstra(s, e))
